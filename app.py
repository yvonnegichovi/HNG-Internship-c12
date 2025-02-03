from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime, timezone

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def index():
    current_utc = datetime.utcnow().replace(microsecond=0)
    return jsonify({
        "email": "yvonnegichovi@gmail.com",
        "current_datetime": current_utc.isoformat() + "Z",
        "github_url": "https://github.com/yvonnegichovi/HNG-Internship-c12"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
