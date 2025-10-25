from flask import request, jsonify
from flask_jwt_extended import JWTManager, create_access_token

def setup_auth(app):
    jwt = JWTManager(app)

    @app.route('/login', methods=['POST'])
    def login():
        username = request.json.get('username')
        password = request.json.get('password')
        if username == 'admin' and password == 'password':
            access_token = create_access_token(identity=username)
            return jsonify(access_token=access_token)
        return jsonify({'msg': 'Bad username or password'}), 401
