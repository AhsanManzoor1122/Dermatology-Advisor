from DBHandler import DBHandler
from sqlalchemy import Column, Integer, String, Text

class Disease(DBHandler.Base):
    __tablename__ = 'disease'
    id = Column(Integer, primary_key=True)
    name = Column(String(25))
    description = Column(Text)
    causes = Column(Text)
    cure = Column(Text)
