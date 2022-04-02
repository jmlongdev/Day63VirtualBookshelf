# import sqlite3

# Creates a connection to a new database. the database is created and stored in the directory
# db = sqlite3.connect('books-collection.db')

# Creates a cursor to control the database created. Cursor is needed to modify the SQlite database
# cursor = db.cursor()

# created table
# NOT NULL means th einput must contain a value and cannot be empty
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, "
#                                     "title varchar(250) NOT NULL UNIQUE,"
#                                     "author varchar(250) NOT NULL, "
#                                     "rating FLOAT NOT NULL)")

# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# TODO Create an SQLite database called new-books-collection.db
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), unique=False, nullable=False)
    rating = db.Column(db.Float, unique=False, nullable=False)

    def __repr__(self):
        return f"<Book {self.title}>"

db.create_all()


# TODO Create a table in this database called books.
# new_book is created from the Book class
new_book = Book(title='Harry Potter', author='J.K Rowling', rating=9.3)

# adds the new book to the database
db.session.add(new_book)

# commits the addition
db.session.commit()

# Read All Records
# all_books = session.query(Book).all()

# Read A Particular Record By Query
book = Book.query.filter_by(title='Harry Potter').first()

# Update A Particular Record By Query
# book_to_update = Book.query.filter_by(title="Harry Potter").first()
# book_to_update_title = "Harry Potter and the Chamber of Secrets"
# db.session.commit()

# Update A Record By PRIMARY KEY
book_id = 1
book_to_update = Book.query.get(book_id)
book_to_update.title = "Harry Potter and the Goblet of Fire"
db.session.commit()

# Delete A Particular Record By PRIMARY KEY
book_id = 2
book_to_delete = Book.query.get(book_id)
db.session.delete(book_to_delete)
db.session.commit()



