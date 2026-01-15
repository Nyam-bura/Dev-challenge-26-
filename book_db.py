from core.table import Table
from core.types import Integer, Text
from core.database import Database

def main():
    db = Database("BookDB")

    books = Table(
        name="books",
        columns={
            "id": Integer(),
            "title": Text(),
            "author": Text(),
            "year": Integer(),
        },
        primary_key = "id",
        unique_keys = ["title"]
    )

    # Author table
    authors = Table(
        name="authors",
        columns={
            "id": Integer(),
            "name": Text(),
            "year": Integer(),
        },
        primary_key = "id",
        unique_keys = ["name"]
    )

    # Insert books
    books.insert({"id": 1, "title": "1984", "author": "George Orwell", "year": 1949})
    books.insert({"id": 2, "title": "Brave New World", "author": "Aldous Huxley", "year": 1932})
    books.insert({"id": 3, "title": "Fahrenheit 451", "author": "Ray Bradbury", "year": 1953})

    authors.insert({"id":1,"name": "George Orwell", "year": 1903})
    authors.insert({"id":2,"name": "Aldous Huxley", "year": 1894})
    authors.insert({"id":3,"name": "Ray Bradbury", "year": 1920})

    books.inner_join(authors, self_column="author", other_column="name")

    # Test invalid insert
    try:
        books.insert({"id": 3, "title": "Fahrenheit 451", "author": "Ray Bradbury", "year": "Nineteen Fifty-Three"})
    except ValueError as e:
        print("Caught error:", e)

    # Show books
    books.show()

    # update book by primary key
    books.update(1, {"year": 1950})

    # Search for a book
    books.search("author", "George Orwell")

    # Delete a book
    books.delete("id", 2)

    # Show books after deletion
    books.show()

if __name__ == "__main__":
    main()
