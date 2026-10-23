from DBHandler import DBHandler
from sqlalchemy import Column, Integer, String, Date, Text


class Users(DBHandler.Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    session = Column(Integer)
    name = Column(String(25))
    email = Column(String(30))
    password = Column(String(20))
    role = Column(String(1))
    gender = Column(String(1))
    contact = Column(String(13))
    dob = Column(Date)
    city = Column(String(25))
    address = Column(Text)
    img_path = Column(Text)
