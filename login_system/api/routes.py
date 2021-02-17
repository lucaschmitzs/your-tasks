from flask import Flask, Blueprint
from .models import Api


api = Blueprint('api', __name__, url_prefix='/api/')


@api.route('/', methods=['GET'])
def get_all():
    return Api().get_all()


@api.route('/<string:id>', methods=['GET'])
def get(id):
    return Api().get(id)


@api.route('/', methods=['POST'])
def post():
    return Api().post()


@api.route('/<string:id>', methods=['PATCH'])
def patch(id):
    return Api().patch(id)


@api.route('/<string:id>', methods=['DELETE'])
def delete(id):
    return Api().delete(id)
