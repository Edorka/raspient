from flask import jsonify, request

from . import api
from .. import db
from ..models.source import Category
from ..schemas.source import source_schema, sources_schema
from binascii import hexlify

"""    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String)
  api_key = db.Column(db.String)"""


@api.route('/sources', methods=['GET'])
def get_sources():
    pass


@api.route('/sources/<int:id>', methods=['GET'])
def get_source(id):
    pass


@api.route('/sources', methods=['POST'])
def create_source():
    json_data = request.get_json()
    if not json_data:
        return jsonify({'message': 'No input data provided'}), 400
    # Validate and deserialize input
    source, errors = source_schema.load(json_data)
    if errors:
        print errors
        return jsonify(errors), 422
    # Create new source
    source.api_key = hexlify(os.urandom(32)) 
    db.session.add(source)
    db.session.commit()
    return jsonify({"message": "Created new source.",
                    "source": source_schema.dump(source).data})

@api.route('/sources/<int:id>', methods=['PUT'])
def update_source(id):
    pass


@api.route('/sources/<int:id>', methods=['DELETE'])
def delete_source(id):
    pass
