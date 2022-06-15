"""The file for handling the cli commands."""
from flask.cli import FlaskGroup

from project import app


cli = FlaskGroup(app)

@cli.command("create_db")
def create_db():
    # db.drop_all()
    # db.create_all()
    # db.session.commit()
    pass


@cli.command("seed_db")
def seed_db():
    # db.session.add(User(email="michael@mherman.org"))
    # db.session.commit()
    pass


if __name__ == "__main__":
    cli()