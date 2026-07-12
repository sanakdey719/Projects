# 💻 Code Compiler - Personal Practice Platform

A lightweight, browser-based code executor for practicing Python, JavaScript, and SQL with ML/DL libraries (pandas, scikit-learn, torch, langchain, etc.).

**Works on Android browser 📱 | Free hosting 🚀 | No setup needed ⚡**

---

## **Features**

✅ **Python execution** - Full standard library + pandas, numpy, scikit-learn, torch, transformers, langchain  
✅ **SQL execution** - SQLite database queries  
✅ **JavaScript execution** - Node.js  
✅ **Code templates** - Quick snippets for common tasks  
✅ **Beautiful UI** - Google Colab style interface  
✅ **Works on Android** - Termux + Browser or deployed URL  
✅ **30-second timeout** - Prevents infinite loops  

---

## **Quick Start**

### **Option 1: Local (Termux)**

```bash
# Install
pkg install python pip
pip install -r requirements.txt

# Run
python main.py

# Access
# Open browser → http://localhost:8000
```

### **Option 2: Deploy on Railway (5 minutes)**

1. Create GitHub repo with these files
2. Push to GitHub
3. Go to railway.app → Connect GitHub → Select repo
4. Done! Get URL and access from anywhere

### **Option 3: Deploy on Render**

1. Go to render.com
2. New Web Service → GitHub repo
3. Build: `pip install -r requirements.txt`
4. Start: `python main.py`
5. Deploy!

---

## **How to Use**

1. **Select language** - Python, JavaScript, or SQL
2. **Write code** - Or use templates
3. **Press Run** - Ctrl+Enter shortcut
4. **See output** - Real-time results

---

## **Supported Libraries**

### **Python**
- **Data**: pandas, numpy, scipy
- **ML**: scikit-learn, matplotlib, seaborn
- **DL**: torch, transformers, langchain
- **APIs**: httpx, requests, pydantic
- **Testing**: pytest

### **JavaScript**
- Full Node.js standard library

### **SQL**
- SQLite (in-memory or file-based)

---

## **Project Structure**

```
code-compiler/
├── main.py           # FastAPI backend
├── index.html        # Frontend UI
├── requirements.txt  # Dependencies
├── Procfile         # Deployment config
├── README.md        # This file
└── SETUP.md         # Detailed setup guide
```

---

## **API Endpoints**

```bash
# Execute Python/JavaScript
POST /api/execute
Body: {"code": "print('hello')", "language": "python"}

# Execute SQL
POST /api/execute-sql
Body: {"query": "SELECT * FROM users;"}

# Health check
GET /health
```

---

## **Mobile Development Workflow**

Using **Acode** on Android:

1. Edit `main.py` and `index.html` in Acode
2. Run in Termux
3. Open http://localhost:8000 in browser
4. Git commit and push from Termux
5. Railway auto-deploys from GitHub

---

## **Limitations**

⚠️ **30-second timeout** - Long-running code will timeout  
⚠️ **No persistent storage** - Databases reset on server restart  
⚠️ **Free tier resources** - May be slower than local  
⚠️ **Heavy libraries** - torch/transformers may take time on first load  

---

## **Troubleshooting**

**Port 8000 already in use?**
```bash
python -c "import socket; s = socket.socket(); s.bind(('', 8001)); print('Use port 8001')"
```

**Dependencies fail to install?**
```bash
pip install torch --index-url https://download.pytorch.org/whl/cpu
```

**CORS errors?**
Already fixed in main.py - should work fine

---

## **Future Ideas**

- [ ] Save/load code snippets
- [ ] Code execution history
- [ ] Jupyter notebook style cells
- [ ] GitHub Gist integration
- [ ] Real-time collaboration (WebSocket)
- [ ] Custom theme support
- [ ] API key management (for LangChain/OpenAI)

---

## **Made with**

- **Backend**: FastAPI + Python
- **Frontend**: HTML5 + CSS3 + Vanilla JS
- **Hosting**: Railway / Render (Free tier)
- **Editor**: Acode (Android)

---

## **License**

Free to use and modify for personal learning. 📚

---

**Happy Coding! 🚀**