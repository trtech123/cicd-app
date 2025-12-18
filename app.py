from flask import Flask

app = Flask(__name__)

MESSAGE = "Hello from version 1 🚀"

@app.route("/")
def home():
    return MESSAGE

@app.route("/health")
def health():
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
