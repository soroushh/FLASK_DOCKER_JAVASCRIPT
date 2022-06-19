"""The file including the flask app."""
from flask import Flask, jsonify
from mappers import User, Address, Student, user_schema
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
        session.add(
            User(
                email=email,
                active=True,
                addresses=[
                    Address(email_address=email)
                ],
                job='student'
            )
        )
        session.commit()

    return jsonify({'message': 'User is added.'})

@app.route('/user/<id1>/<id2>')
def change_addresses(id1, id2):
    """Changes the addresses of the users."""
    with Session(create_db_engine(db_url=current_app.config['SQLALCHEMY_DATABASE_URI'])) as session:
        user_1 = session.query(User).filter(user_schema.primary_key.columns[0] == int(id1)).first()
        user_2 = session.query(User).filter(user_schema.primary_key.columns[0] == int(id2)).first()
        user_1.addresses.extend(user_2.addresses)
        session.commit()

    return jsonify({'message': 'addresses changed.'})

@app.route('/user/<id>')
def find_user(id):
    """Finds a user."""
    with Session(create_db_engine(db_url=current_app.config['SQLALCHEMY_DATABASE_URI'])) as session:
        user = session.query(User).filter(User.id == int(id)).first()

    return jsonify({'email': user.email})

@app.route('/student/add')
def add_student():
    """Adds a student."""
    with Session(create_db_engine(db_url=current_app.config['SQLALCHEMY_DATABASE_URI'])) as session:
        session.add(Student(
            number=14,
            email='b@b.com',
            active=True,
            job='student',
            addresses=[Address(email_address='b@b.com')]
        ))
        session.commit()

    return jsonify({'message': 'addresses changed.'})
