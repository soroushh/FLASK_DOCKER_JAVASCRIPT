"""Includes the user model."""
from typing import List

from dataclasses import dataclass, field
from models.address import Address


@dataclass
class User:
    id: int = field(init=False)
    email: str
    active: bool
    addresses: List[Address] = field(default_factory=list)