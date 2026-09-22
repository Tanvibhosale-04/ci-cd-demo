from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello from CI/CD Demo!"


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=False)