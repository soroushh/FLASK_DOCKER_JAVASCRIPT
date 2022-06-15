"""Includes the db definition."""
from sqlalchemy import create_engine
from flask import current_app

def create_db_engine(db_url):
    """Creates an engine based on a db url."""
    return create_engine(db_url, echo=True, future=True)