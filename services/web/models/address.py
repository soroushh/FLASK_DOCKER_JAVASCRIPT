"""The definition of the Address model."""
from dataclasses import dataclass, field


@dataclass
class Address:
    id: int = field(init=False)
    user_id: int = field(init=False)
    email_address: str = None