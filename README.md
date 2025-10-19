# 💬 Personal Chatbot

A modern, production-ready chatbot built with Flask and Google's Generative AI (Gemini). Features a beautiful, responsive UI and is ready for deployment on Render.com.

## ✨ Features

- 🤖 Powered by Google Gemini AI
- 💬 Modern, responsive chat interface
- 🔒 Secure session management
- 🚀 Production-ready with Gunicorn
- 📱 Mobile-friendly design
- ⚡ Fast and lightweight

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Google Generative AI API key ([Get one here](https://makersuite.google.com/app/apikey))

### Local Development

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd personal-chatbot
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Mac/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set environment variables**
   
   **Windows (PowerShell):**
   ```powershell
   $env:GEMINI_API_KEY="your-api-key-here"
   $env:SECRET_KEY="your-secret-key-here"
   $env:PORT=5000
   ```
   
   **Mac/Linux:**
   ```bash
   export GEMINI_API_KEY="your-api-key-here"
   export SECRET_KEY="your-secret-key-here"
   export PORT=5000
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open your browser**
   Navigate to `http://localhost:5000`

## 🌐 Deploy to Render.com

### Step 1: Push to GitHub
```bash
git add .
git commit -m "Ready for deployment"
git push origin master
```

### Step 2: Create a Render Web Service

1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub repository
4. Configure the service:
   - **Name**: `personal-chatbot` (or your preferred name)
   - **Region**: Choose closest to your users
   - **Branch**: `master` (or your default branch)
   - **Root Directory**: Leave empty
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn --bind 0.0.0.0:$PORT app:app`

### Step 3: Set Environment Variables

In the Render dashboard, add these environment variables:

| Variable | Value | Description |
|----------|-------|-------------|
| `GEMINI_API_KEY` | Your API key | **Required** - Get from Google AI Studio |
| `SECRET_KEY` | Random string | **Required** - Generate with: `python -c "import secrets; print(secrets.token_hex(32))"` |
| `GEMINI_MODEL` | `gemini-1.5-flash` | Optional - AI model to use |
| `SESSION_COOKIE_SECURE` | `True` | Optional - For HTTPS cookies |

### Step 4: Deploy

Click **"Create Web Service"** and Render will:
- Build your application
- Install dependencies
- Start the service
- Provide a public URL (e.g., `https://personal-chatbot.onrender.com`)

### Step 5: Test Your Deployment

1. Visit your Render URL
2. Test the `/health` endpoint: `https://your-app.onrender.com/health`
3. Try chatting with your bot!

## 📁 Project Structure

```
personal-chatbot/
├── app.py                 # Main Flask application
├── chatbot_config.py      # Bot configuration (name, persona)
├── requirements.txt       # Python dependencies
├── Procfile              # Render deployment config
├── runtime.txt           # Python version specification
├── templates/
│   └── index.html        # Chat interface
└── static/
    └── style.css         # Modern styling
```

## 🔧 Configuration

### Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `GEMINI_API_KEY` | ✅ Yes | - | Google Gemini API key |
| `SECRET_KEY` | ✅ Yes (prod) | `dev-secret-change-me` | Flask session secret |
| `GEMINI_MODEL` | ❌ No | `gemini-1.5-flash` | AI model version |
| `SESSION_COOKIE_SECURE` | ❌ No | `False` | Enable secure cookies (HTTPS) |
| `PORT` | ❌ No | `5000` | Server port (auto-set by Render) |

### Customizing Your Bot

Edit `chatbot_config.py` to customize:

```python
BOT_NAME = "Your Bot Name"
BOT_PERSONA = """Your custom persona and instructions"""
```

## 🔒 Security Notes

- ✅ Never commit API keys or secrets to Git
- ✅ Use environment variables for all sensitive data
- ✅ Generate strong `SECRET_KEY` for production
- ✅ Enable `SESSION_COOKIE_SECURE` on Render (HTTPS)

## 📊 Monitoring

- **Health Check**: `/health` endpoint returns `{"status": "ok"}`
- **Render Dashboard**: Monitor logs, metrics, and deployment status
- **Auto-Deploy**: Enabled by default on Git push

## 🐛 Troubleshooting

### Build Fails on Render
- Check Python version in `runtime.txt`
- Verify all dependencies in `requirements.txt`
- Check build logs in Render dashboard

### App Crashes on Start
- Verify `GEMINI_API_KEY` is set correctly
- Check `SECRET_KEY` is set
- Review logs: `render logs -s <service-name>`

### Session Not Working
- Sessions now use signed cookies (no filesystem dependency)
- Ensure `SECRET_KEY` is set and consistent

### API Rate Limits
- Free tier: 60 requests/minute
- Upgrade to paid tier for higher limits
- Consider caching responses

## 📝 License

MIT License - feel free to use this for personal or commercial projects!

## 🤝 Contributing

Contributions welcome! Please feel free to submit a Pull Request.

---

**Made with ❤️ using Flask and Google Gemini AI**
