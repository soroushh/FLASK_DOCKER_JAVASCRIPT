"""The definition of the user schema."""
from sqlalchemy import Table, Column, Integer, String, ForeignKey, Boolean
from db import meta

user = Table(
    'users',
    meta,
    Column('id', Integer, primary_key=True),
    Column('email', String(50)),
    Column('job', String(50)),
    Column('active', Boolean)
)