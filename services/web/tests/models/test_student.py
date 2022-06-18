"""Tests related to Student model."""
from models.student import Student

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