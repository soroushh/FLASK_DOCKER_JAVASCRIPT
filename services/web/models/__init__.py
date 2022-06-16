"""The definition of the application models."""
from sqlalchemy.orm import registry, relationship

from .address import Address
from .db_schemas.address import address as address_schema
from .db_schemas.user import user as user_schema
from .user import User

mapper_registry = registry()
mapper_registry.map_imperatively(Address, address_schema)
mapper_registry.map_imperatively(User, user_schema, properties={
    'addresses': relationship(Address, lazy="joined", backref='user', order_by=address_schema.c.id),
})