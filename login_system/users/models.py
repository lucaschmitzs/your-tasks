from flask import jsonify, request, session, redirect
from passlib.hash import pbkdf2_sha256
from .collection import collection
import uuid


class User:

    def start_session(self, user):
        """ Function responsible to register the user into the session """

        del user['password']
        session['logged_in'] = True
        session['user'] = user
        return jsonify(user), 200

    def signup(self):
        """ Function responsible to create an account and after that, automatically log in the user """

        user = {
            "_id": uuid.uuid4().hex,
            "name": request.form.get('name'),
            "username": request.form.get('username'),
            "email": request.form.get('email'),
            "password": request.form.get('password')
        }

        # Encrypt the password
        user['password'] = pbkdf2_sha256.encrypt(user['password'])

        # Check for existing email addres and username
        if collection.find_one({"email": user['email']}):
            return jsonify({"error": "Email already in use"}), 400
        elif collection.find_one({"username": user['username']}):
            return jsonify({"error": "Username already in use"}), 400

        # if success on the insert into the database, then log in the user
        if collection.insert_one(user):
            return self.start_session(user)

        return jsonify({"error": "Signup failed"}), 400

    def logout(self):
        """ Function responsible to clear the session (log out the user) """

        session.clear()
        return redirect('/')

    def login(self):
        """ Function responsible to log in the user when the account is already setup """

        user = collection.find_one({
            "username": request.form.get('username')
        })

        # Password validation for log in parameters
        if user and pbkdf2_sha256.verify(request.form.get('password'), user['password']):
            return self.start_session(user)

        return jsonify({"error": "Invalid login credentials"}), 401

    def update(self):
        """ Function responsible for update user information when pleased """

        # Find user logged in
        user_loggedin = collection.find_one({
            "username": session['user']['username']
        })

        # Get the new user informations from form
        updated_user = {
            "name": request.form.get('name'),
            "username": request.form.get('username'),
            "email": request.form.get('email'),
            "password": request.form.get('password')
        }

        # Encrypt the password
        updated_user['password'] = pbkdf2_sha256.encrypt(
            updated_user['password'])

        # Validate only if the email already exists in the database when the new email and the current email differ
        if user_loggedin['email'] != updated_user['email']:
            if collection.find_one({"email": updated_user['email']}):
                return jsonify({"error": "Email already in use"}), 400

        # Validate only if the username already exists in the database when the new username and the current username differ
        if user_loggedin['username'] != updated_user['username']:
            if collection.find_one({"username": updated_user['username']}):
                return jsonify({"error": "Username already in use"}), 400

        # If the update ocur with no errors, then update the information in session
        if collection.find_one_and_update({"username": user_loggedin['username']},
                                          {'$set': {'name': updated_user['name'],
                                                    'username': updated_user['username'],
                                                    'email': updated_user['email'],
                                                    'password': updated_user['password']}}):
            return self.start_session(updated_user)

        return jsonify({"error": "Update failed"}), 400

    def reset(self):
        """ Function responsible when the user wants reset some information when forgot the credentials """

        # Find the user using the email from the form
        user = collection.find_one({
            "email": request.form.get('email')
        })

        # If the email dosen't exists, then return a error
        if not user:
            return jsonify({"error": "Email not found"}), 404

        # If email exists, obtain the rest of the user information on the form
        else:
            reset_user = {
                "username": request.form.get('username'),
                "password": request.form.get('password')
            }

            reset_user['password'] = pbkdf2_sha256.encrypt(
                reset_user['password'])

            # Validate only if the username already exists in the database when the new username and the current username differ
            if user['username'] != reset_user['username']:
                if collection.find_one({"username": reset_user['username']}):
                    return jsonify({"error": "Username already in use"}), 400

            collection.find_one_and_update({"email": user['email']},
                                           {'$set': {'username': reset_user['username'],
                                                     'password': reset_user['password']}})

        return jsonify({"success": "Reset with success"}), 200
