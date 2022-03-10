import sqlalchemy
from .base import metadata

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column("email", sqlalchemy.String(32), unique=True),
    sqlalchemy.Column("username", sqlalchemy.String(32), unique=True),
    sqlalchemy.Column("hashed_password", sqlalchemy.String(128)),
    sqlalchemy.Column("role", sqlalchemy.String(5))

)
