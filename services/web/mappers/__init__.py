"""The mappers between models and schemas."""
from sqlalchemy.orm import registry, relationship

from models.address import Address
from models.db_schemas.address import address as address_schema
from models.db_schemas.user import user as user_schema
from models.user import User

mapper_registry = registry()
mapper_registry.map_imperatively(Address, address_schema)
mapper_registry.map_imperatively(User, user_schema, properties={
    'addresses': relationship(Address, lazy="joined", backref='user', order_by=address_schema.c.id),
})