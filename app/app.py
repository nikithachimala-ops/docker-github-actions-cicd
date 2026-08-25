from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Docker + GitHub Actions CI/CD</h1>
    <h2>Application successfully deployed!</h2>
    <p>Running on AWS EC2 using Docker and GitHub Actions.</p>
    """

@app.route("/health")
def health():
    return {"status": "healthy"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)