from .. import db


class Source(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String)
    api_key = db.Column(db.String)

    def __repr__(self):
        return 'source {}>'.format(self.id)
