from flask import Flask, jsonify, request, session, redirect
from passlib.hash import pbkdf2_sha256
from .collection import collection
import uuid


class User:

    def start_session(self, user):
        del user['password']
        session['logged_in'] = True
        session['user'] = user
        return jsonify(user), 200

    def signup(self):
        user = {
            "_id": uuid.uuid4().hex,
            "name": request.form.get('name'),
            "username": request.form.get('username'),
            "email": request.form.get('email'),
            "password": request.form.get('password')
        }

        # Encrypt the password
        user['password'] = pbkdf2_sha256.encrypt(user['password'])

        # Check for existing email addres
        if collection.find_one({"email": user['email']}):
            return jsonify({"error": "Email already in use"}), 400
        elif collection.find_one({"username": user['username']}):
            return jsonify({"error": "Username already in use"}), 400

        if collection.insert_one(user):
            return self.start_session(user)

        return jsonify({"error": "Signup failed"}), 400

    def signout(self):
        session.clear()
        return redirect('/')

    def login(self):
        user = collection.find_one({
            "username": request.form.get('username')
        })

        if user and pbkdf2_sha256.verify(request.form.get('password'), user['password']):
            return self.start_session(user)

        return jsonify({"error": "Invalid login credentials"}), 401

    def update(self):
        user_loggedin = collection.find_one({
            "username": session['user']['username']
        })

        updated_user = {
            "name": request.form.get('name'),
            "username": request.form.get('username'),
            "email": request.form.get('email'),
            "password": request.form.get('password')
        }

        # Encrypt the password
        updated_user['password'] = pbkdf2_sha256.encrypt(
            updated_user['password'])


        if user_loggedin['email'] != updated_user['email']:
            if collection.find_one({"email": updated_user['email']}):
                return jsonify({"error": "Email already in use"}), 400
        if user_loggedin['username'] != updated_user['username']:
            if collection.find_one({"username": updated_user['username']}):
                return jsonify({"error": "Username already in use"}), 400

        if collection.find_one_and_update({"username": user_loggedin['username']},
                                     {'$set': {'name': updated_user['name'],
                                               'username': updated_user['username'],
                                               'email': updated_user['email']}}):
            return self.start_session(updated_user)

        return jsonify({"error": "Update failed"}), 401
