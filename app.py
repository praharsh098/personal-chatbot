from flask import Flask, render_template, request, jsonify, session
import google.generativeai as genai
from chatbot_config import BOT_NAME, BOT_PERSONA
from flask_session import Session

genai.configure(api_key="Your_api_key")

app = Flask(__name__)
app.secret_key = "your_secret_key"
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

model = genai.GenerativeModel("gemini-1.5-flash")

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
    chat = model.start_chat(history=history)
    response = chat.send_message(user_input)

    # Update history
    history.append({"role": "user", "parts": [user_input]})
    history.append({"role": "model", "parts": [response.text]})
    session["chat"] = history

    return jsonify({"response": response.text})
