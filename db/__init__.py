from .users import users
from .services import services
from .reports import reports
from .ML_emotion import ML_emotion
from .ML_cluster_center import ML_cluster_center
from .ML_regular_entries import ML_regular_entries
from .base import metadata, engine

metadata.create_all(bind=engine)