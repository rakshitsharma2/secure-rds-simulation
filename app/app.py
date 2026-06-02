from flask import Flask
import pymysql
import os

app = Flask(__name__)

@app.route("/")
def home():
    try:
        conn = pymysql.connect(
            host="localhost",
            user="appuser",
            password="apppass123",
            database="securedb"
        )

        conn.close()

        return "Connected to Secure MySQL Database"

    except Exception as e:
        return f"Database Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)