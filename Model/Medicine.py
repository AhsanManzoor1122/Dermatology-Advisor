from DBHandler import DBHandler
from sqlalchemy import Column, Integer, String


class Medicine(DBHandler.Base):
    __tablename__ = 'medicine'
    id = Column(Integer, primary_key=True)
    rx_id = Column(Integer)
    name = Column(String(25))
    strength = Column(Integer)
    dosage = Column(String(5))
    days = Column(Integer)
