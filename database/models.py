from sqlalchemy import Column, Date, Float, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Rate(Base):
    __tablename__ = 'rate'

    id = Column(Integer, primary_key=True)
    date_rate = Column(Date)
    EUR = Column(Float)
    USD = Column(Float)
