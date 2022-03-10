from contextlib import contextmanager

from databases import Database
from sqlalchemy import create_engine, orm, MetaData
from sqlalchemy.ext.declarative import declarative_base

EE_DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/kitsune_db?charset=utf8mb4"

engine = create_engine(EE_DATABASE_URL, pool_recycle=3600)
Base = declarative_base()
database = Database(EE_DATABASE_URL)
metadata = MetaData()


def init_sessionmaker():
    """Создает глобальную сессию."""
    global Session
    Session = orm.sessionmaker(bind=engine)


@contextmanager
def session_scope():
    """Удобная обертка для открытия безопасного сессий БД."""
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
