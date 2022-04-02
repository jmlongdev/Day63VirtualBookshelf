from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# Creates the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///virtual-library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# this is the class that each created object, or book is to be
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), unique=False, nullable=False)
    rating = db.Column(db.Float, unique=False, nullable=False)


db.create_all()


@app.route('/', methods=["GET"])
def home():
    all_books = db.session.query(Book).all()
    return render_template('index.html', books=all_books)


# Adds a book to the database
@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        new_book = Book(title=request.form['title'], author=request.form['author'], rating=request.form['rating'])
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('add.html')


# Edits the book's rating
@app.route("/edit", methods=["GET", 'POST'])
def edit():
    if request.method == 'POST':
        book_id = request.form['id']
        book_to_update = Book.query.get(book_id)
        book_to_update.rating = request.form['rating']
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = Book.query.get(book_id)
    return render_template('edit.html', book=book_selected)


# Delete the book
@app.route('/delete')
def delete():
    if request.method == "GET":
        book_id = request.args.get('id')
        book_to_delete = Book.query.get(book_id)
        db.session.delete(book_to_delete)
        db.session.commit()
        return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

