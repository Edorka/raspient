#! /usr/bin/env python

import os

from flask_script import Manager

from app import create_app, db


app = create_app(os.getenv('APP_CONFIG', 'default'))
manager = Manager(app)


@manager.shell
def make_shell_context():
    return dict(app=app, db=db)


@manager.command
def createdb():
    from app.models import reading, source
    # import the rest of the models aswell
    db.create_all()

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
  return response


if __name__ == '__main__':
    manager.run()


