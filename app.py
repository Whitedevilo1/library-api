from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from models import db, Book

app = Flask(__name__)
CORS(app) 


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)
with app.app_context():
    db.create_all()

# Specifying-Server 
@app.route('/')
def frontend():
    return send_from_directory('static', 'index.html')

#  CRUD APIs
@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([b.to_dict() for b in books]), 200

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.query.get_or_404(book_id)
    return jsonify(book.to_dict()), 200

@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    new_book = Book(
        title=data['title'],
        author=data['author'],
        year_published=data.get('year_published'),
        genre=data.get('genre')
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify(new_book.to_dict()), 201

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = Book.query.get_or_404(book_id)
    data = request.get_json()
    book.title = data.get('title', book.title)
    book.author = data.get('author', book.author)
    book.year_published = data.get('year_published', book.year_published)
    book.genre = data.get('genre', book.genre)
    db.session.commit()
    return jsonify(book.to_dict()), 200

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Book deleted'}), 200

#  Run Server
if __name__ == '__main__':
    app.run(debug=True)
