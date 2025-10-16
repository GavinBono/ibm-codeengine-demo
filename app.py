from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.get("/")
def home():
    return "Hello from Gavin’s IBM Cloud Demo! 🚀"

@app.get("/health")
def health():
    return jsonify(status="ok", platform="IBM Code Engine")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8080"))
    app.run(host="0.0.0.0", port=port)
