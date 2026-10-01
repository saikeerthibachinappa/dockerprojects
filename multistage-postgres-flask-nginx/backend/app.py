from flask import Flask, jsonify, request
import psycopg2
import os

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("POSTGRES_DB")
DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")


def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )


@app.route("/api/")
def home():
    return jsonify({
        "message": "PostgreSQL Docker App"
    })


@app.route("/api/users", methods=["GET"])
def users():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, name FROM users ORDER BY id")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify([
        {
            "id": row[0],
            "name": row[1]
        }
        for row in rows
    ])


@app.route("/api/users", methods=["POST"])
def add_user():
    data = request.get_json()

    name = data.get("name")

    if not name:
        return jsonify({
            "error": "Name is required"
        }), 400

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users (name) VALUES (%s) RETURNING id, name",
        (name,)
    )

    user = cursor.fetchone()

    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({
        "id": user[0],
        "name": user[1]
    }), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)