## Chatbot (Flask + Google Generative AI)

### Prerequisites
- Python 3.10+
- Google Generative AI API key

### Setup
1. Create and activate a virtual environment.
2. Set environment variables.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

### Run locally
Set environment variables (PowerShell example):

```powershell
$env:GEMINI_API_KEY="<your-key>"
$env:SECRET_KEY="dev-secret"
$env:GEMINI_MODEL="gemini-1.5-flash"
$env:SESSION_TYPE="filesystem"
$env:PORT=5000
python app.py
```

Open `http://localhost:5000`.

### Production
- Exposes a `/health` endpoint.
- Use `gunicorn` with the provided `Procfile`:

```bash
gunicorn --bind 0.0.0.0:${PORT:-8000} app:app
```

### Configuration
- `GEMINI_API_KEY` (required)
- `SECRET_KEY` (required in prod)
- `GEMINI_MODEL` (optional, defaults to `gemini-1.5-flash`)
- `SESSION_TYPE` (defaults `filesystem`)

### Notes
- Do not commit real secrets. Use environment variables in production.
