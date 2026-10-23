from DBHandler import DBHandler
from sqlalchemy import Column, Integer, String, Date, Text,DateTime


class Doctor(DBHandler.Base):
    __tablename__ = 'doctor'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    specialization = Column(String(25))
    experience = Column(Integer)
    isonline = Column(Integer)
    login_time=Column(DateTime)