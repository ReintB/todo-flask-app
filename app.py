import os
import sqlite3
from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-secret-key")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INSTANCE_DIR = os.path.join(BASE_DIR, "instance")
DATABASE = os.path.join(INSTANCE_DIR, "todo.db")


def get_db_connection():
    os.makedirs(INSTANCE_DIR, exist_ok=True)
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    connection = get_db_connection()
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            completed INTEGER NOT NULL DEFAULT 0,
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    connection.commit()
    connection.close()


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        if not title:
            flash("Tugas tidak boleh kosong.", "danger")
        else:
            connection = get_db_connection()
            connection.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
            connection.commit()
            connection.close()
            flash("Tugas berhasil ditambahkan.", "success")
            return redirect(url_for("index"))

    connection = get_db_connection()
    tasks = connection.execute(
        "SELECT id, title, completed FROM tasks ORDER BY completed ASC, id DESC"
    ).fetchall()
    connection.close()
    return render_template("index.html", tasks=tasks)


@app.post("/toggle/<int:task_id>")
def toggle_task(task_id):
    connection = get_db_connection()
    connection.execute(
        "UPDATE tasks SET completed = CASE completed WHEN 0 THEN 1 ELSE 0 END WHERE id = ?",
        (task_id,),
    )
    connection.commit()
    connection.close()
    return redirect(url_for("index"))


@app.post("/delete/<int:task_id>")
def delete_task(task_id):
    connection = get_db_connection()
    connection.execute("DELETE FROM tasks WHERE id = ? AND completed = 1", (task_id,))
    connection.commit()
    connection.close()
    flash("Tugas selesai dihapus.", "success")
    return redirect(url_for("index"))


init_db()


if __name__ == "__main__":
    app.run(debug=True)
