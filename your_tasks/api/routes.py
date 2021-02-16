
from flask import Flask, Blueprint
from .models import Api


api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/get_all', methods=['GET'])
def get_all():
    return Api().get_all()


@api.route('/get/<string:id>', methods=['GET'])
def get(id):
    return Api().get(id)


@api.route('/post', methods=['POST'])
def post():
    return Api().post()
