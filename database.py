from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from get_settings import settings

host = settings.app_db__host
user = settings.app_db__user
password = settings.app_db__password

SQLALCHEMY_URL = f'postgresql+psycopg2://{user}:{password}@{host}/app'

engine = create_engine(SQLALCHEMY_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close_all()