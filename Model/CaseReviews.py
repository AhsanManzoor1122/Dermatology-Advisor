from DBHandler import DBHandler
from sqlalchemy import Column, Integer, String, Text


class CaseReviews(DBHandler.Base):
    __tablename__ = 'case_reviews'
    id = Column(Integer, primary_key=True)
    case_id = Column(Integer)
    possible_disease = Column(String(25))
    observation = Column(Text)
