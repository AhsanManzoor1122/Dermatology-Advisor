from DBHandler import DBHandler
from sqlalchemy import Column, Integer, Text, DATETIME


class CaseRX(DBHandler.Base):
    __tablename__ = 'case_rx'
    id = Column(Integer, primary_key=True)
    observation = Column(Text)
    date_time = Column(DATETIME)
