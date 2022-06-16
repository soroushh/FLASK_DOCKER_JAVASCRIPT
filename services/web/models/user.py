"""Includes the user model."""
from typing import List

from dataclasses import dataclass, field
from sqlalchemy.orm import registry, relationship
from models.db_schemas.user import user as user_schema
from models.db_schemas.address import address as address_schema

mapper_registry = registry()

# user_table = Table(
#     'users',
#     meta,
#     Column('id', Integer, primary_key=True),
#     Column('email', String(50)),
#     Column('active', Boolean)
# )
#
# address = Table(
#     'address',
#     meta,
#     Column('id', Integer, primary_key=True),
#     Column('user_id', Integer, ForeignKey('users.id')),
#     Column('email_address', String(50)),
# )

@dataclass
class Address:
    id: int = field(init=False)
    user_id: int = field(init=False)
    email_address: str = None


@dataclass
class User:
    id: int = field(init=False)
    email: str
    active: bool
    addresses: List[Address] = field(default_factory=list)

mapper_registry.map_imperatively(User, user_schema, properties={
    'addresses': relationship(Address, lazy="joined", backref='user', order_by=address_schema.c.id),
})

mapper_registry.map_imperatively(Address, address_schema)