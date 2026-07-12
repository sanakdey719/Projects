from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
import subprocess
import json
import os
from pathlib import Path
import signal
import sqlite3
from contextlib import contextmanager

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CodeRequest(BaseModel):
    code: str
    language: str = "python"

class SQLRequest(BaseModel):
    query: str
    db_name: str = "test.db"

def timeout_handler(signum, frame):
    raise TimeoutError("Code execution timed out (30 seconds limit)")

@app.post("/api/execute")
async def execute_code(request: CodeRequest):
    """Execute Python or JavaScript code"""
    try:
        if request.language == "python":
            # Python execution with timeout
            process = subprocess.Popen(
                ["python", "-c", request.code],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                timeout=30
            )
            stdout, stderr = process.communicate(timeout=30)
            
            if stderr:
                return {
                    "success": False,
                    "output": stderr,
                    "language": "python"
                }
            return {
                "success": True,
                "output": stdout,
                "language": "python"
            }
        
        elif request.language == "javascript":
            process = subprocess.Popen(
                ["node", "-e", request.code],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                timeout=30
            )
            stdout, stderr = process.communicate(timeout=30)
            
            if stderr:
                return {
                    "success": False,
                    "output": stderr,
                    "language": "javascript"
                }
            return {
                "success": True,
                "output": stdout,
                "language": "javascript"
            }
        
        else:
            raise HTTPException(status_code=400, detail="Language not supported")
            
    except subprocess.TimeoutExpired:
        return {
            "success": False,
            "output": "⏱️ Execution timed out (30 second limit)",
            "language": request.language
        }
    except Exception as e:
        return {
            "success": False,
            "output": f"Error: {str(e)}",
            "language": request.language
        }

@app.post("/api/execute-sql")
async def execute_sql(request: SQLRequest):
    """Execute SQL queries"""
    try:
        conn = sqlite3.connect(request.db_name)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        # Split multiple statements
        statements = request.query.split(";")
        results = []
        
        for statement in statements:
            statement = statement.strip()
            if not statement:
                continue
            
            cursor.execute(statement)
            
            if statement.strip().upper().startswith("SELECT"):
                rows = cursor.fetchall()
                results.append({
                    "query": statement,
                    "result": [dict(row) for row in rows]
                })
            else:
                conn.commit()
                results.append({
                    "query": statement,
                    "result": f"Executed. Rows affected: {cursor.rowcount}"
                })
        
        conn.close()
        return {
            "success": True,
            "results": results
        }
    except Exception as e:
        return {
            "success": False,
            "output": f"SQL Error: {str(e)}"
        }

@app.get("/")
async def root():
    """Serve the frontend"""
    return FileResponse("index.html")

@app.get("/health")
async def health():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)