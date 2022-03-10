import sqlalchemy
from .base import metadata

reports = sqlalchemy.Table(
    "reports",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column("service_id", sqlalchemy.Integer),
    sqlalchemy.Column("status", sqlalchemy.Integer),
    sqlalchemy.Column("time", sqlalchemy.String(32))
)