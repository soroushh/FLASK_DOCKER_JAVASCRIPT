"""Includes the user model."""
from sqlalchemy import Table, Column, Integer, String, ForeignKey, Boolean, MetaData
from sqlalchemy.orm import registry
from dataclasses import dataclass
from dataclasses import field

mapper_registry = registry()
meta = MetaData()

user_table = Table(
    'users',
    meta,
    Column('id', Integer, primary_key=True),
    Column('email', String(50)),
    Column('active', Boolean)
)

@dataclass
class User:
    id: int = field(init=False)
    email: str
    active: bool

mapper_registry.map_imperatively(User, user_table)