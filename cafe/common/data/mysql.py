from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from cafe.config import settings

engine = create_engine(settings.db.uri, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
