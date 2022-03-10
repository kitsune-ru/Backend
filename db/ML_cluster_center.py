import sqlalchemy
from .base import metadata

ML_cluster_center = sqlalchemy.Table(
    "ML_cluster_center",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column("tags", sqlalchemy.String(32)),
    sqlalchemy.Column("density", sqlalchemy.Float),
    sqlalchemy.Column("embedding", sqlalchemy.String(32)),
    sqlalchemy.Column("distantion", sqlalchemy.String(32))
)