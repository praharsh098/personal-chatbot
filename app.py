from flask import Flask, render_template, request, jsonify, session
import os
import google.generativeai as genai
from chatbot_config import BOT_NAME, BOT_PERSONA

# Load configuration from environment
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
MODEL_NAME = os.environ.get("GEMINI_MODEL", "gemini-1.5-flash")
SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-change-me")

if not GEMINI_API_KEY:
    # Fail fast with a clear error for missing API key in production
    raise RuntimeError("GEMINI_API_KEY environment variable is not set.")

genai.configure(api_key=GEMINI_API_KEY)

app = Flask(__name__)
app.secret_key = SECRET_KEY
# Use Flask's built-in session (signed cookies) - production ready
app.config["SESSION_COOKIE_SECURE"] = os.environ.get("SESSION_COOKIE_SECURE", "False").lower() == "true"
app.config["SESSION_COOKIE_HTTPONLY"] = True
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"

model = genai.GenerativeModel(MODEL_NAME)

@app.route("/")
def index():
    if "chat" not in session:
        session["chat"] = [{"role": "user", "parts": [BOT_PERSONA]}]
    return render_template("index.html", bot_name=BOT_NAME)

@app.route("/chat", methods=["POST"])
def chat_reply():
    user_input = request.json["message"]

    # Restore chat from session
    history = session.get("chat", [])
    try:
        chat = model.start_chat(history=history)
        response = chat.send_message(user_input)
        text = response.text
    except Exception as exc:
        # Return a friendly error while not exposing internals
        text = "Sorry, I couldn't process that request right now. Please try again."

    # Update history
    history.append({"role": "user", "parts": [user_input]})
    history.append({"role": "model", "parts": [text]})
    session["chat"] = history

    return jsonify({"response": text})

@app.get("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
