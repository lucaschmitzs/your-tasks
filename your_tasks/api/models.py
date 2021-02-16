from flask import jsonify, request
from bson.json_util import dumps
from passlib.hash import pbkdf2_sha256
from your_tasks.login_system.collection import collection
import uuid


class Api():

    def get_all(self):
        result = collection.find()
        return dumps(result)

    def get(self, id):
        result = collection.find_one({'_id': id})
        if result:
            return dumps(result)
        else:
            return jsonify({'error': 'id not found'}), 404

    def post(self):
        id = uuid.uuid4().hex
        name = request.json['name']
        username = request.json['username']
        email = request.json['email']
        password = request.json['password']
        if name and username and email and password and request.method == 'POST':
            password = pbkdf2_sha256.encrypt(password)
            collection.insert({'_id': id,
                               'name': name,
                               'username': username,
                               'email': email,
                               'password': password})
            return jsonify({'success': 'user added'}), 200
        else:
            return jsonify({'error': 'incorrect parameters'}), 400

    def put(self, id):
        pass

    def delete(self, id):
        pass
