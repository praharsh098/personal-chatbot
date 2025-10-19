# 🚀 Render.com Deployment Checklist

Follow this checklist to ensure a smooth deployment to Render.com.

## ✅ Pre-Deployment Checklist

- [x] Session storage fixed (using signed cookies instead of filesystem)
- [x] Dependencies updated (removed Flask-Session)
- [x] Modern UI implemented
- [x] `runtime.txt` added for Python version
- [x] `Procfile` configured for Gunicorn
- [x] `.gitignore` created to protect sensitive files
- [x] README updated with deployment instructions

## 📋 Before You Deploy

### 1. Get Your API Keys
- [ ] Obtain Google Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
- [ ] Generate a secure SECRET_KEY:
  ```bash
  python -c "import secrets; print(secrets.token_hex(32))"
  ```

### 2. Test Locally
- [ ] Set environment variables locally
- [ ] Run `python app.py`
- [ ] Test chat functionality
- [ ] Test `/health` endpoint
- [ ] Verify UI looks good

### 3. Commit Your Changes
- [ ] Stage all changes: `git add .`
- [ ] Commit: `git commit -m "Ready for deployment"`
- [ ] Push to GitHub: `git push origin main`

## 🌐 Deploy to Render.com

### Step 1: Create Render Account
- [ ] Sign up at [render.com](https://render.com)
- [ ] Connect your GitHub account

### Step 2: Create Web Service
- [ ] Click "New +" → "Web Service"
- [ ] Connect your repository
- [ ] Select branch: `main` (or `master`)

### Step 3: Configure Service
- [ ] **Name**: `personal-chatbot` (or your choice)
- [ ] **Region**: Choose closest to users
- [ ] **Runtime**: Python 3
- [ ] **Build Command**: `pip install -r requirements.txt`
- [ ] **Start Command**: `gunicorn --bind 0.0.0.0:$PORT app:app`
- [ ] **Plan**: Free (or choose paid for better performance)

### Step 4: Set Environment Variables
Add these in Render dashboard:

- [ ] `GEMINI_API_KEY` = Your Google Gemini API key
- [ ] `SECRET_KEY` = Your generated secret key
- [ ] `GEMINI_MODEL` = `gemini-1.5-flash` (optional)
- [ ] `SESSION_COOKIE_SECURE` = `True` (for HTTPS)

### Step 5: Deploy
- [ ] Click "Create Web Service"
- [ ] Wait for build to complete (2-5 minutes)
- [ ] Check build logs for errors

## 🧪 Post-Deployment Testing

### Test Your Live App
- [ ] Visit your Render URL (e.g., `https://personal-chatbot.onrender.com`)
- [ ] Test health endpoint: `https://your-app.onrender.com/health`
- [ ] Send a test message to the chatbot
- [ ] Verify UI displays correctly
- [ ] Test on mobile device
- [ ] Check browser console for errors

### Common Issues
- [ ] If build fails: Check Python version in `runtime.txt`
- [ ] If app crashes: Verify environment variables are set
- [ ] If session issues: Confirm SECRET_KEY is set
- [ ] If slow responses: Normal for free tier (spins down after inactivity)

## 📊 Monitor Your App

### Render Dashboard
- [ ] Check deployment status
- [ ] Monitor logs for errors
- [ ] View metrics (requests, response time)
- [ ] Set up email alerts for crashes

### Health Checks
- [ ] Render auto-checks `/health` endpoint
- [ ] Verify it returns `{"status": "ok"}`
- [ ] Check logs for health check requests

## 🔄 Continuous Deployment

### Auto-Deploy Enabled
- [ ] Render will auto-deploy on push to main branch
- [ ] Test by making a small change and pushing
- [ ] Verify new deployment appears in dashboard

### Manual Deploy
If needed, you can manually trigger a deployment:
1. Go to Render dashboard
2. Click "Manual Deploy"
3. Select branch and click "Deploy"

## 🔒 Security Reminders

- [ ] Never commit API keys to Git
- [ ] Use environment variables for all secrets
- [ ] Keep SECRET_KEY secure and don't share it
- [ ] Enable HTTPS (automatic on Render)
- [ ] Review Render security settings

## 📈 Performance Tips

### Free Tier Limitations
- App spins down after 15 minutes of inactivity
- First request after spin-down takes ~30 seconds
- 750 hours/month free

### Upgrade Considerations
- Paid tier: No spin-down, faster cold starts
- Better for production use
- More consistent performance

## 🆘 Need Help?

### Common Commands
```bash
# View logs
render logs -s personal-chatbot

# Check service status
render services list

# Get service details
render services show personal-chatbot
```

### Resources
- [Render Documentation](https://render.com/docs)
- [Flask Deployment Guide](https://flask.palletsprojects.com/en/latest/deploying/)
- [Google Gemini API Docs](https://ai.google.dev/docs)

## ✨ Success!

Once all items are checked, your chatbot is live and ready to use!

Your app URL: `https://your-app.onrender.com`

---

**Last Updated**: $(date)
**Status**: Ready for Deployment ✅
