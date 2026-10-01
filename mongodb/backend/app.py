from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
import os

app = Flask(__name__)
CORS(app)

MONGO_HOST = os.getenv("MONGO_HOST", "localhost")
MONGO_PORT = int(os.getenv("MONGO_PORT", "27017"))

client = MongoClient(
    host=MONGO_HOST,
    port=MONGO_PORT,
    username="root",
    password="example",
    authSource="admin"
)

db = client["taskdb"]
tasks = db["tasks"]


@app.route("/api/tasks", methods=["GET"])
def get_tasks():

    result = []

    for task in tasks.find():
        result.append({
            "id": str(task["_id"]),
            "name": task["name"]
        })

    return jsonify(result)


@app.route("/api/tasks", methods=["POST"])
def add_task():

    data = request.json
    name = data.get("name")

    if not name:
        return jsonify({"error": "Task name is required"}), 400

    task = {
        "name": name
    }

    inserted = tasks.insert_one(task)

    return jsonify({
        "id": str(inserted.inserted_id),
        "name": name
    }), 201


@app.route("/api/tasks/<task_id>", methods=["DELETE"])
def delete_task(task_id):

    from bson import ObjectId

    tasks.delete_one({
        "_id": ObjectId(task_id)
    })

    return jsonify({
        "message": "Task deleted"
    })


@app.route("/api/health")
def health():

    try:
        client.admin.command("ping")

        return jsonify({
            "application": "healthy",
            "database": "connected"
        })

    except Exception as e:

        return jsonify({
            "application": "healthy",
            "database": "not connected",
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )