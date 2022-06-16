"""The file for handling the cli commands."""
import os

from flask.cli import FlaskGroup
from sqlalchemy.orm import Session

from db import meta, create_db_engine
from models import User
from project import app

cli = FlaskGroup(app)

@cli.command("create_db")
def create_db():
    engine = create_db_engine(os.getenv('DATABASE_URL'))
    # meta.drop_all(engine)
    meta.create_all(engine)


@cli.command("seed_db")
def seed_db():
    with Session(create_db_engine(db_url=os.getenv('DATABASE_URL'))) as session:
        session.add(User(email='a@a.com', active=True))
        session.commit()


if __name__ == "__main__":
    cli()