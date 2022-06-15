"""Includes the user model."""
from sqlalchemy import Table, Column, Integer, String, ForeignKey, Boolean, MetaData
from sqlalchemy.orm import registry
from dataclasses import dataclass
from dataclasses import field
from sqlalchemy.orm import relationship
from typing import List

mapper_registry = registry()
meta = MetaData()

user_table = Table(
    'users',
    meta,
    Column('id', Integer, primary_key=True),
    Column('email', String(50)),
    Column('active', Boolean)
)

address = Table(
    'address',
    meta,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('email_address', String(50)),
)

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

mapper_registry.map_imperatively(User, user_table, properties={
    'addresses': relationship(Address, lazy="joined", backref='user', order_by=address.c.id),
})

mapper_registry.map_imperatively(Address, address)