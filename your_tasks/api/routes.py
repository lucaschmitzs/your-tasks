
from flask import Flask, Blueprint
from .models import Api


api = Blueprint('api', __name__, url_prefix='/api/')


@api.route('/', methods=['GET'])
def get_all():
    return Api().get_all()

z
@api.route('/<string:id>', methods=['GET'])
def get(id):
    return Api().get(id)


@api.route('/', methods=['POST'])
def post():
    return Api().post()


@api.route('/<string:id>', methods=['PUT'])
def put(id):
    return Api().put(id)


@api.route('/<string:id>', methods=['DELETE'])
def delete(id):
    return Api().delete(id)
