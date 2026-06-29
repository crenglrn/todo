from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    env = os.getenv("ENVIRONMENT", "Local Development")
    return f"<h1>To-Do Delivery App 🐋</h1><p>Release Status: Live in <b>{env}</b></p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)