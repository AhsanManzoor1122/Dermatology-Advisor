from DBHandler import DBHandler
from sqlalchemy import Column, Integer, DATETIME, Text


class Case(DBHandler.Base):
    __tablename__ = 'case'
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer)
    doctor_id = Column(Integer)
    disease_id = Column(Integer)
    is_prescribed = Column(Integer)
    is_rated = Column(Integer)
    app_response = Column(Integer)
    rx_id = Column(Integer)
    date_time = Column(DATETIME)
    img_path = Column(Text)
