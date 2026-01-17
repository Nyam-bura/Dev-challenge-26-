# app.py
from flask import Flask, render_template, request, redirect, url_for
from core.database import Database
from core.types import Integer, Text

from core.table import Table

app = Flask(__name__)

# Initialize the database and books table
db = Database("LibraryDB")
books = db.create_table(
    "books",
    columns={
        "id": Integer(),
        "title": Text(),
        "author": Text(),
        "year": Integer(),
    },
    primary_key="id",
    unique_keys=["title"]
)

books.insert({"id": 1, "title": "1984", "author": "George Orwell", "year": 1949})
books.insert({"id": 2, "title": "Brave New World", "author": "Aldous Huxley","year":1932})

# Routes

@app.route("/")
def index():
    return render_template("index.html", books=books.rows)

@app.route("/add", methods=["POST"])
def add_book():
    try:
        title = request.form["title"]
        author = request.form["author"]
        year = int(request.form["year"])
        books.insert({"title": title, "author": author, "year": year})
    except Exception as e:
        return f"Error: {e}"
    return redirect(url_for("index"))

@app.route("/update/<int:id>", methods=["POST"])
def update_book(id):
    try:
        updates = {}
        if request.form.get("title"):
            updates["title"] = request.form["title"]
        if request.form.get("author"):
            updates["author"] = request.form["author"]
        if request.form.get("year"):
            updates["year"] = int(request.form["year"])
        books.update(id, updates)
    except Exception as e:
        return f"Error: {e}"
    return redirect(url_for("index"))

@app.route("/delete/<int:id>")
def delete_book(id):
    books.delete("id", id)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
