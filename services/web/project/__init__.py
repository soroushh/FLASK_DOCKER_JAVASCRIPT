"""The file including the flask app."""
from flask import Flask, jsonify
from db import db
from models.user import User


app = Flask(__name__)
app.config.from_object("project.config.Config")
db.init_app(app)


@app.route("/")
def hello_world():
    return jsonify(hello="world")

@app.route('/user/add/<email>')
def add_user(email):
    """Adds a user to db."""
    db.session.add(User(email=email))
    db.session.commit()

    return jsonify({'message': 'User is added.'})