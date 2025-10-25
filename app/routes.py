from flask import request, jsonify
from app.models import db, Book
from flask_jwt_extended import jwt_required

def create_routes(app):

    @app.route('/')
    def home():
        return "Welcome to Book API"

    @app.route('/books', methods=['GET'])
    def get_books():
        books = Book.query.all()
        return jsonify([{'id': b.id, 'title': b.title, 'author': b.author, 'year': b.year} for b in books])

    @app.route('/books', methods=['POST'])
    @jwt_required()
    def add_book():
        data = request.get_json()
        new_book = Book(title=data['title'], author=data['author'], year=data.get('year'))
        db.session.add(new_book)
        db.session.commit()
        return jsonify({'message': 'Book added successfully'}), 201
