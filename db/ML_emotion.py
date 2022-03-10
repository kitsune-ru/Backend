import sqlalchemy
from .base import metadata

ML_emotion = sqlalchemy.Table(
    "ML_emotion",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column("name", sqlalchemy.String(32)),
    sqlalchemy.Column("embedding", sqlalchemy.String(32))
)