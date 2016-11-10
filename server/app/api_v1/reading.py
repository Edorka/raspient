from flask import jsonify, request

from . import api
from .. import db
from ..models.reading import Reading
from ..schemas.reading import reading_schema, readings_schema
import datetime


@api.route('/readings', methods=['GET'])
@api.route('/source/<int:source_id>/readings', methods=['GET'])
def get_readings(source_id=None):
    search = Reading.query
    if source_id is not None:
        search = search.filter_by(source_id=source_id)
    search = search.order_by(Reading.moment.desc())
    result = readings_schema.dump(search.all())
    return jsonify(items=result.data, count=Reading.query.count())


@api.route('/readings/<int:id>', methods=['GET'])
def get_reading(id):
    pass


@api.route('/readings', methods=['POST'])
@api.route('/source/<int:source_id>/readings', methods=['POST'])
def create_reading(source_id):
    json_data = request.get_json()
    if not json_data:
        return jsonify({'message': 'No input data provided'}), 400
    # Validate and deserialize input
    reading, errors = reading_schema.load(json_data)
    if errors:
        print errors
        return jsonify(errors), 422
    # Create new reading
    if source_id is not None:
        reading.source_id = source_id
    db.session.add(reading)
    db.session.commit()
    return jsonify({"message": "Created new reading.",
                    "reading": reading_schema.dump(reading).data})
