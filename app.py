from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Lead Extractor Backend (placeholder for full app.py code)"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
