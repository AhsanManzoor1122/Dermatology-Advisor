

from sqlalchemy import null
from Model.Doctor import Doctor
from Model.Patient import Patient
from Model.Users import Users
from DBHandler import DBHandler
from DBHandler import return_session
import DBHandler
from flask import jsonify
import Extentions
from sqlalchemy.orm import exc
from sqlalchemy.exc import SQLAlchemyError
from Controller import UsersController

session = return_session()


async def sign_up_patient(name, email, password, gender, city):
    try:
        #user_id, status_code = await add_user()
        #patient = Patient(user_id=user_id['user_id'], name=name, gender=gender, city=city)
        #session.add(patient)
        session.commit()
        return {"message": "Patient Signup successful"}, 200
    except Exception as ex:
        session.rollback()
        return {"error": str(ex)}, 500
    finally:
        session.close()


def get_patient(user_id):
    try:
        patient_data = session.query(Patient).filter_by(user_id=user_id).first()
        patient = {
            "id": patient_data.id,
            "name": patient_data.name,
            "gender": patient_data.gender,
            "contact": patient_data.contact,
            "dob": patient_data.dob,
            "city": patient_data.city,
            "address": patient_data.address,
            "img_path": patient_data.img_path
        }
        return {"patient":patient}
    except Exception as ex:
        return {"error": str(ex)}, 500
    finally:
        session.close()



def update_patient(user_id, name, email, password, gender, contact, dob, city, address, img_path):
    try:
        patient = session.query(Patient).filter_by(user_id=user_id).first()
        if patient:
            user = session.query(Users).get(user_id)
            if name:
                user.name = name
            if email:
                user.email = email
            if password:
                user.password = password
            if gender:
                user.gender = gender
            if contact:
                user.contact = contact
            if dob:
                user.dob = dob
            if city:
                user.city = city
            if address:
                user.address = address
            if img_path:
                user.img_path = img_path
            session.commit()
            return {"message": "Patient updated successfully"}, 200
        else:
            return {"error": "Patient ID not found"}, 404
    except SQLAlchemyError as ex:

        session.rollback()
        return {"error": str(ex)}, 500
    finally:
        session.close()
