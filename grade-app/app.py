import os
from decimal import Decimal, InvalidOperation
from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET", "dev-secret")

DB_HOST = os.getenv("DB_HOST")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME", "grade_app")

def get_conn():
    return pymysql.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME,
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=True,
    )

@app.get("/")
def enter():
    return render_template("enter.html")

@app.post("/submit")
def submit():
    student_id = (request.form.get("student_id") or "").strip()
    grade_raw = (request.form.get("grade") or "").strip()

    if not student_id:
        flash("Student ID is required.")
        return redirect(url_for("enter"))

    try:
        grade = Decimal(grade_raw)
    except (InvalidOperation, ValueError):
        flash("Grade must be a number.")
        return redirect(url_for("enter"))

    if grade < 0 or grade > 100:
        flash("Grade must be between 0 and 100.")
        return redirect(url_for("enter"))

    sql = """
    INSERT INTO grades (student_id, grade)
    VALUES (%s, %s)
    ON DUPLICATE KEY UPDATE grade = VALUES(grade)
    """

    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (student_id, str(grade)))

    return redirect(url_for("grades"))

@app.get("/grades")
def grades():
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT student_id, grade FROM grades ORDER BY student_id ASC")
            rows = cur.fetchall()

            cur.execute("SELECT AVG(grade) AS avg_grade FROM grades")
            avg_row = cur.fetchone()

    avg_grade = avg_row["avg_grade"]
    avg_grade_display = f"{avg_grade:.2f}" if avg_grade is not None else "N/A"
    return render_template("grades.html", rows=rows, avg_grade=avg_grade_display)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
