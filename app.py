from flask import Flask, render_template, request, jsonify
import json
import random

app = Flask(__name__)

# Load intents and model
with open("intents.json") as file:
    intents = json.load(file)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    # Use your model to predict the intent and fetch a response
    for intent in intents["intents"]:
        if user_message.lower() in [p.lower() for p in intent["patterns"]]:
            return jsonify({"response": random.choice(intent["responses"])})
    return jsonify({"response": "Sorry, I don't understand that."})

if __name__ == "__main__":
    app.run(debug=True)
