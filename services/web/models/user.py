"""Includes the user model."""
class User:
    def __init__(
            self,
            email,
            active,
            job,
            addresses=None,
            id=None
    ):
        self.email = email
        self.active = active
        self.job = job
        self.addresses = addresses or []
        self.id = id