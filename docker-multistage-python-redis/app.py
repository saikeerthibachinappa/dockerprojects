from flask import Flask, jsonify
import redis
import os

app = Flask(__name__)

# Get Redis hostname from environment variable
redis_host = os.getenv("REDIS_HOST", "localhost")

# Connect to Redis
r = redis.Redis(
    host=redis_host,
    port=6379,
    decode_responses=True
)


@app.route("/")
def home():
    return jsonify({
        "message": "Docker Redis App",
        "status": "running"
    })


@app.route("/count")
def count():
    current_count = r.incr("counter")

    return jsonify({
        "count": current_count
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )