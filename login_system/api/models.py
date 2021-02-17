from flask import jsonify, request
from bson.json_util import dumps
from passlib.hash import pbkdf2_sha256
from login_system.users.collection import collection
import uuid


class Api():

    def get_all(self):
        """ Function responsible to get all the user from database """
        result = collection.find()
        return dumps(result)

    def get(self, id):
        """ Function responsible to get the user from a specific id """
        result = collection.find_one({'_id': id})
        if result:
            return dumps(result)
        else:
            return jsonify({'error': 'id not found'}), 404

    def post(self):
        """ Function responsible to create a new user, with all the parameters being requires """
        id = uuid.uuid4().hex
        name = request.json['name']
        username = request.json['username']
        email = request.json['email']
        password = request.json['password']

        # Check for existing email addres and username
        if collection.find_one({'username': username}):
            return jsonify({"error": "Username already in use"}), 400

        elif collection.find_one({'email': email}):
            return jsonify({"error": "Email already in use"}), 400

        # Chek if all the parameters are in the request
        elif name and username and email and password and request.method == 'POST':
            password = pbkdf2_sha256.encrypt(password)
            collection.insert({'_id': id,
                               'name': name,
                               'username': username,
                               'email': email,
                               'password': password})
            return jsonify({'success': 'user added'}), 200
        else:
            return jsonify({'error': 'Incorrect parameters'}), 400

    def patch(self, id):
        """ Function responsible for update the user, not being required all the parameters """
        user = collection.find_one({'_id': id})
        parameters = ['name', 'username', 'email', 'password']
        user_update = {}

        # For loop for check which parameters are being used
        for params in parameters:
            # If any
            if params in request.json:
                # Create a dictionary for dynamically randle the request
                user_update.setdefault(params, request.json[f'{params}'])
                # If username in parameters
                if params == 'username':
                    # If current username differ from request username, check for unique username in the database
                    if user['username'] != request.json['username']:
                        if collection.find_one({'username': request.json['username']}):
                            return jsonify({"error": "Username already in use"}), 400
                # If email in parameters                            
                if params == 'email':
                    # If current email differ from request email, check for unique email in the database
                    if user['email'] != request.json['email']:
                        if collection.find_one({'email': request.json['email']}):
                            return jsonify({"error": "Email already in use"}), 400
                # If password in parameters, then encrypt               
                if params == 'password':
                    user_update.update(
                        {'password': pbkdf2_sha256.encrypt(request.json['password'])})

        for key, value in user_update.items():
            collection.update_one({'_id': id},
                                  {'$set': {key: value}})

        return jsonify({'success': 'user updated'}), 200

    def delete(self, id):
        """ Function responsible on delete a specific user """
        if collection.delete_one({'_id': id}):
            return jsonify({'success': 'user deleted'}), 200
        else:
            return jsonify({'error': 'id not found'}), 404
