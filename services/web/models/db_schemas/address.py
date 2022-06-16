"""The definition of the address schema."""
from sqlalchemy import Table, Column, Integer, String, ForeignKey, Boolean
from db import meta

address = Table(
    'address',
    meta,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('email_address', String(50)),
)