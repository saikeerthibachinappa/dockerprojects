from flask import Flask
import os
import psycopg2

app = Flask(__name__)


def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "db"),
        database=os.getenv("POSTGRES_DB", "appdb"),
        user=os.getenv("POSTGRES_USER", "appuser"),
        password=os.getenv("POSTGRES_PASSWORD", "apppassword")
    )


@app.route("/")
def home():
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("SELECT message FROM messages LIMIT 1")
        result = cur.fetchone()

        cur.close()
        conn.close()

        message = result[0] if result else "No message found"

        return f"""
        <h1>Docker Challenge 4</h1>
        <p>Message from PostgreSQL: {message}</p>
        """

    except Exception as e:
        return f"Database connection failed: {e}", 500


@app.route("/health")
def health():
    return {"status": "UP"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)