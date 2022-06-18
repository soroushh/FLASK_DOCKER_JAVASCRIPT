"""Tests related to Student model."""
from models.student import Student
from db import create_db_engine, meta
from mappers import User, Address, Student
from sqlalchemy.orm import Session

def test_model():
    """."""
    student = Student(
        id=1,
        email='a@a.com',
        active=True,
        number=15,
        job='student'
    )

    assert isinstance(student, Student)

    assert student.number == 15


def test_adding_student_adds_user_and_student():
    """."""
    engine = create_db_engine(db_url='sqlite:///')
    meta.drop_all(engine)
    meta.create_all(engine)
    with Session(engine) as session:
        users = session.query(User).all()
        students = session.query(Student).all()
        addresses = session.query(Address).all()

        assert len(students) == 0
        assert len(users) == 0
        assert len(addresses) == 0

        session.add(
            Student(
                email='a@a.com',
                active=True,
                job='student',
                number=10,
                addresses=[
                    Address(
                        email_address='b@b.com'
                    )
                ]
            )
        )
        session.commit()

        users = session.query(User).all()
        students = session.query(Student).all()
        addresses = session.query(Address).all()

    assert len(users) == 1

    assert isinstance(users[0], User)
    assert users[0].id == 1
    assert users[0].email == 'a@a.com'
    assert users[0].job == 'student'

    assert isinstance(students[0], Student)
    assert isinstance(students[0], User)
    assert len(students) == 1
    assert students[0].id == 1
    assert students[0].number == 10

    assert len(addresses) == 1
    assert isinstance(addresses[0], Address)
    assert addresses[0].id == 1
    assert addresses[0].email_address == 'b@b.com'
    assert addresses[0].user_id == 1
