from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from handlers.config import db_url

engine = create_engine(db_url)
SessionLocal = sessionmaker(engine, expire_on_commit=False)
