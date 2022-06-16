"""The definition of the Address model."""
from dataclasses import dataclass, field
from models.db_schemas.address import address as address_schema
from sqlalchemy.orm import registry


@dataclass
class Address:
    id: int = field(init=False)
    user_id: int = field(init=False)
    email_address: str = None

mapper_registry = registry()

mapper_registry.map_imperatively(Address, address_schema)