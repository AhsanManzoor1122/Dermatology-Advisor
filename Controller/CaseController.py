import json
from sqlalchemy import null
from datetime import datetime
from Model.Doctor import Doctor
from Model.Users import Users
from Model.Case import Case
from Model.Patient import Patient
from Model.CaseImg import CaseImg
from DBHandler import DBHandler
from DBHandler import return_session
import DBHandler
from flask import jsonify
import Extentions
from sqlalchemy.orm import exc
from sqlalchemy.exc import SQLAlchemyError
from Controller import UsersController
session = return_session()


def get_cases(user_id):
    try:
        row = session.query(Patient).filter_by(user_id=user_id).first()
        if row:
            patient_id = row.id
            cases = session.query(Case).filter_by(patient_id=patient_id).all()
            if cases:
                case_data = {}
                for index, value in enumerate(cases):
                    data = {
                        'id': value.id,
                        'patient_id': value.patient_id,
                        'doctor_id': value.doctor_id,
                        'disease_id': value.disease_id,
                        'is_prescribed': value.is_prescribed,
                        'is_rated': value.is_rated,
                        'app_response': value.app_response,
                        'rx_id': value.rx_id,
                        'date_time': value.date_time,
                        'img_path': value.img_path
                    }
                    case_data[index] = data

                return case_data, 200
            else:
                return "No case found", 404
        else:
            return "Patient not found", 404
    except Exception as ex:
        return {"error": str(ex)}, 500
    finally:
        session.close()


def set_case(user_id, disease_id, img_path):
    try:
        row = session.query(Patient).filter_by(user_id=user_id).first()
        patient_id = row.id
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entity = Case(patient_id=patient_id, disease_id=disease_id, is_prescribed=0, is_rated=0,
                      date_time=current_datetime, img_path=img_path)
        session.add(entity)
        session.commit()
        return {
            "id": entity.id,
            "patient_id": entity.patient_id,
            "doctor_id": entity.doctor_id,
            "disease_id": entity.disease_id,
            "is_prescribed": entity.is_prescribed,
            "is_rated": entity.is_rated,
            "date_time": entity.date_time,
            "img_path": entity.img_path
        }, 200
    except Extentions as ex:
        session.rollback()
        return {"error": str(ex)}, 500
    finally:
        session.close()