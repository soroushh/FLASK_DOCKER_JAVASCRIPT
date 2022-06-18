from .user import user
from db import meta
from sqlalchemy import Table, Column, Integer, String, ForeignKey, Boolean

students = Table(
    'students',
    meta,
    Column('id', Integer, ForeignKey("users.id"), primary_key=True),
    Column('number', Integer),
)