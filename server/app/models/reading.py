from .. import db
from source import Source
from datetime import datetime


class Reading(db.Model):

    moment = db.Column(db.DateTime, primary_key=True, default=datetime.utcnow)
    source_id = db.Column(db.Integer, db.ForeignKey('source.id'), 
			  primary_key=True, default=1)
    source = db.relationship('Source', lazy=True)
    temperature = db.Column(db.Float)
    humidity = db.Column(db.Float)

    def __repr__(self):
        return 'Reading {}>'.format(self.source)
