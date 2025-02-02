from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return jsonify({
        "email": "yvonnegichovi@gmail.com",
        "current_datetime": datetime.utcnow().isoformat() + "Z",
        "github_url": "https://github.com/yvonnegichovi/HNG-Internship-c12"
    })

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
