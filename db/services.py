import sqlalchemy
from .base import metadata

services = sqlalchemy.Table(
    "services",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column("service_name", sqlalchemy.String(32), unique=True),
    sqlalchemy.Column("description", sqlalchemy.String(256)),
    sqlalchemy.Column("status", sqlalchemy.Integer)
)
