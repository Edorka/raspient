from flask import jsonify, request

from . import api
from .. import db
from ..models.competition import competition
from ..schemas.competition import competition_schema, competitions_schema


@api.route('/competitions', methods=['GET'])
def get_competitions():
    pass


@api.route('/competitions/<int:id>', methods=['GET'])
def get_competition(id):
    pass


@api.route('/competitions', methods=['POST'])
def create_competition():
    pass


@api.route('/competitions/<int:id>', methods=['PUT'])
def update_competition(id):
    pass


@api.route('/competitions/<int:id>', methods=['DELETE'])
def delete_competition(id):
    pass
