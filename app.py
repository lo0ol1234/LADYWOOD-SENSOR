from flask import Flask, request, jsonify, render_template
import time

app = Flask(__name__)

latest_reading = {"level": None, "timestamp": None}

@app.route("/")
def index():
    return render_template("index.html", reading=latest_reading)

@app.route("/api/level", methods=["POST"])
def receive_level():
    global latest_reading
    data = request.json
    level = data.get("level")
    timestamp = time.time()

    latest_reading = {
        "level": level,
        "timestamp": timestamp
    }

    return jsonify({"status": "ok"})

@app.route("/api/latest", methods=["GET"])
def get_latest():
    return jsonify(latest_reading)

if __name__ == "__main__":
    app.run()

