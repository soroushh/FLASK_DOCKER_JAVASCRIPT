"""The tests related to the User model."""
from db import create_db_engine, meta
from mappers import User, Address
from sqlalchemy.orm import Session


def test_object():
    """Tests we can add a user to the db."""
    engine = create_db_engine(db_url='sqlite:///')
    meta.drop_all(engine)
    meta.create_all(engine)
    with Session(engine) as session:
        session.add(
            User(
                email='a@a.com',
                active=True,
                addresses=[
                    Address(
                        email_address='b@b.com'
                    )
                ]
            )
        )
        session.commit()

        user = session.query(User).filter(User.email == 'a@a.com').first()
    assert isinstance(user, User)
    assert user.email == 'a@a.com'
    assert user.id == 1
    assert user.active is True
    assert len(user.addresses) == 1
    assert user.addresses[0].user_id == 1
    assert user.addresses[0].id == 1