import sqlalchemy
from .base import metadata

ML_regular_entries = sqlalchemy.Table(
    "ML_regular_entries",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column("text", sqlalchemy.String(32)),
    sqlalchemy.Column("label", sqlalchemy.Integer),
    sqlalchemy.Column("embedding", sqlalchemy.String(32))
)