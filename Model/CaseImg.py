from DBHandler import DBHandler
from sqlalchemy import Column, Integer, Text


class CaseImg(DBHandler.Base):
    __tablename__ = 'case_img'
    id = Column(Integer, primary_key=True)
    case_id = Column(Integer)
    img_path = Column(Text)
