from .. import ma
from ..models.reading import Reading


class ReadingSchema(ma.ModelSchema):

    class Meta:
        model = Reading


reading_schema = ReadingSchema()
readings_schema = ReadingSchema(many=True)
