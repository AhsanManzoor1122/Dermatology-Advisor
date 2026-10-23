from DBHandler import DBHandler
from sqlalchemy import Column, Integer, Text, DATETIME

class Messages(DBHandler.Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True)
    case_id=Column(Integer)
    case_id=Column(Integer)
    sid=Column(Integer)
    rid=Column(Integer)
    message=Column(Text)
    date_time=Column(DATETIME)
