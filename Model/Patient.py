from sqlalchemy.orm import relationship

from DBHandler import DBHandler
from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey


class Patient(DBHandler.Base):
    __tablename__ = 'patient'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))



