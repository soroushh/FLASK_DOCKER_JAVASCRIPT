"""The definition of student model."""
from .user import User

class Student(User):
    """."""
    def __init__(
            self,
            number,
            email,
            active,
            job,
            addresses=None,
            id=None
    ):
        self.number = number

        super().__init__(
            email=email,
            active=active,
            job=job,
            addresses=addresses,
            id=id
        )
