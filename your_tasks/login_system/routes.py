from flask import Flask, Blueprint
from .models import User

user = Blueprint('user', __name__)


@user.route('/user/signup/', methods=['POST'])
def signup():
    return User().signup()


@user.route('/user/logout/')
def logout():
    return User().logout()


@user.route('/user/login/', methods=['POST'])
def login():
    return User().login()


@user.route('/user/update/', methods=['POST'])
def update():
    return User().update()


@user.route('/user/reset/', methods=['POST'])
def reset():
    return User().reset()
