# 🚀 Code Compiler - Setup & Deployment Guide

## **Local Testing (Acode + Termux)**

### 1. Setup Termux
```bash
# Install Python & pip
pkg install python pip git

# Clone or create project folder
mkdir code-compiler
cd code-compiler
```

### 2. Create Files
Copy the 3 files into Termux:
- `main.py`
- `index.html`
- `requirements.txt`

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Server
```bash
python main.py
```

### 5. Access from Android
- Open Chrome/Firefox
- Go to: `http://localhost:8000`
- Start coding!

---

## **Deploy on Railway (Free)**

### **Option 1: GitHub + Railway (Recommended)**

#### Step 1: Create GitHub Repo
1. Go to github.com → New Repository
2. Name: `code-compiler`
3. Upload files:
   - `main.py`
   - `index.html`
   - `requirements.txt`
   - Create `.gitignore`: Add `__pycache__/`, `.env`, `*.db`
   - Create `Procfile` (add below)

#### Step 2: Create Procfile
```
web: python main.py
```

#### Step 3: Deploy on Railway
1. Go to https://railway.app
2. Login with GitHub
3. Click "Create New Project"
4. Select "Deploy from GitHub repo"
5. Choose your `code-compiler` repo
6. Railway auto-detects Python
7. Add environment variable (optional):
   - KEY: `PYTHONUNBUFFERED`
   - VALUE: `1`
8. Deploy! ✅

#### Step 4: Access
Railway gives you a URL like: `https://code-compiler-xyz.up.railway.app`

Access from Android: Open that URL in Chrome

---

## **Deploy on Render (Alternative)**

### **Using GitHub**

1. Go to https://render.com
2. Login/Signup
3. Click "New Web Service"
4. Connect GitHub → Select repo
5. Fill details:
   - **Name**: `code-compiler`
   - **Language**: Python
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python main.py`
6. Deploy!

---

## **GitHub Pages Deployment (Frontend Only)**

If you only want the UI on GitHub Pages + backend elsewhere:

1. Create `gh-pages` branch
2. Move `index.html` to root
3. Update API calls in JS to point to your backend URL
4. Push to `gh-pages` branch
5. Access: `https://yourusername.github.io/code-compiler/`

---

## **Local Development Tips**

### Edit in Acode
1. Open Acode on Android
2. Open `main.py` and `index.html`
3. Edit directly
4. Run `python main.py` in Termux
5. Refresh browser

### Git Sync from Android
```bash
# In Termux
git add .
git commit -m "Update code"
git push origin main
```

---

## **Troubleshooting**

### Port already in use
```bash
python -c "import socket; s = socket.socket(); s.bind(('', 8000)); s.close()"
```

### Dependencies too heavy
If torch/transformers fail to install:
```bash
# Install lighter version
pip install torch --index-url https://download.pytorch.org/whl/cpu
```

### CORS issues
Already handled in `main.py` - should work cross-origin

### SQL database issues
SQLite databases created in `/tmp` directory - persist locally

---

## **Features & Shortcuts**

- **Ctrl+Enter** or **Cmd+Enter** = Run code
- **Clear Output** = Clear results
- **Clear Code** = Clear editor
- **Templates** = Quick code snippets
- **30s timeout** = Prevent infinite loops

---

## **API Endpoints**

```
POST /api/execute
Body: { "code": "...", "language": "python|javascript" }
Response: { "success": bool, "output": "...", "language": "..." }

POST /api/execute-sql
Body: { "query": "...", "db_name": "test.db" }
Response: { "success": bool, "results": [...] }

GET /health
Response: { "status": "ok" }
```

---

## **Next Steps**

1. ✅ Deploy backend on Railway/Render
2. ✅ Test from Android browser
3. ✅ Add more libraries as needed
4. ✅ Create custom code snippets
5. ✅ Add user authentication (optional)
6. ✅ Save code snippets to localStorage (frontend)

**আপনার জন্য সবকিছু প্রস্তুত! 🚀**
