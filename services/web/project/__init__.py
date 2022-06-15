"""The file including the flask app."""
from flask import Flask, jsonify
from models.user import User
from db import create_db_engine
from sqlalchemy.orm import Session
from flask import current_app

app = Flask(__name__)
app.config.from_object("project.config.Config")


@app.route("/")
def hello_world():
    return jsonify(hello="world")

@app.route('/user/add/<email>')
def add_user(email):
    """Adds a user to db."""
    with Session(create_db_engine(db_url=current_app.config['SQLALCHEMY_DATABASE_URI'])) as session:
        session.add(User(email=email, active=True))
        session.commit()

    return jsonify({'message': 'User is added.'})