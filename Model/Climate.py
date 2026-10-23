from DBHandler import DBHandler
from sqlalchemy import Column, Integer, String


class Climate(DBHandler.Base):
    __tablename__ = 'climate'
    id = Column(Integer, primary_key=True)
    area = Column(String(25))
    temperature = Column(Integer)
    humidity = Column(Integer)
