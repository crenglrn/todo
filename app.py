from flask import Flask
import os

app = Flask(__name__)

@app.py
def home():
    # Grabs a variable from the cloud settings, defaults to "Development"
    env = os.getenv("ENVIRONMENT", "Development")
    return f"<h1>To-Do Delivery App 🐋</h1><p>Status: Live in <b>{env}</b></p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)