"""Includes the user model."""
class User:
    def __init__(self, email, active, addresses=None, id=None):
        self.email = email
        self.active = active
        self.addresses = addresses
        self.id = id