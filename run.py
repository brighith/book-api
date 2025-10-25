from flask import Flask
from app.models import db
from app.routes import create_routes
from app.auth import setup_auth

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your_secret_key'

db.init_app(app)
create_routes(app)
setup_auth(app)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
