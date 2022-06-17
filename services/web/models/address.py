"""The definition of the Address model."""
class Address:
    def __init__(self,email_address, id=None, user_id=None, ):
        self.id = id
        self.email_address = email_address
        self.user_id = user_id