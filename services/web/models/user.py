"""Includes the user model."""
from typing import List

from dataclasses import dataclass, field
from sqlalchemy.orm import registry, relationship
from models.db_schemas.user import user as user_schema
from models.db_schemas.address import address as address_schema
from models.address import Address

mapper_registry = registry()

@dataclass
class User:
    id: int = field(init=False)
    email: str
    active: bool
    addresses: List[Address] = field(default_factory=list)

mapper_registry.map_imperatively(User, user_schema, properties={
    'addresses': relationship(Address, lazy="joined", backref='user', order_by=address_schema.c.id),
})