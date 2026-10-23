from sqlalchemy import null
from Model.Doctor import Doctor
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


# async def add_doctor(name, email, password, gender, dob,
#                      city, address, img_path, specialization,
#                      experience, isonline,session):
#     try:
#         user_id, status_code = await add_user(email=email, password=password, role='D')
#
#         entity = Doctor(user_id=user_id['user_id'], name=name,
#                         gender=gender, dob=dob, city=city, address=address,
#                         img_path=img_path, specialization=specialization,
#                         experience=experience, isonline=isonline,session=session)
#         session.add(entity)
#         session.commit()
#         session.close()
#         return {"message": "Doctor added successfully"}, 200
#     except Exception as ex:
#         session.rollback()
#         return {"error": str(ex)}, 500
#     finally:
#         session.close()


def get_all_doctor():
    try:
        doctors = session.query(Doctor).all()
        user = session.query(Users).filter_by(role='p').all()
        doc_list = [{"id": doctor.id,
                     "user_id": doctor.user_id,
                     "name": user.name,
                     # "gender": doctor.gender,
                     # "dob": doctor.dob,
                     # "city": doctor.city,
                     # "address": doctor.address,
                     # "img_path": doctor.img_path,
                     "specialization": doctor.specialization,
                     "isonline": doctor.isonline
                     } for doctor in doctors]
        return {"data": doc_list}, 200
    except Exception as ex:
        return {"error": str(ex)}, 500
    finally:
        session.close()


def get_doctor(user_id):
    try:
        doctor_data = session.query(Doctor).filter_by(user_id=user_id).first()
        doctor = {
            "id": doctor_data.id,
            "user_id": doctor_data.user_id,
            "name": doctor_data.name,
            "gender": doctor_data.gender,
            "dob": doctor_data.dob,
            "city": doctor_data.city,
            "address": doctor_data.address,
            "img_path": doctor_data.img_path,
            "specialization": doctor_data.specialization,
            "isonline": doctor_data.isonline,
            "session": doctor_data.session
        }
        return {"doctor": doctor}
    except Exception as ex:
        return {"error": str(ex)}, 500
    finally:
        session.close()


def update_doctor(did, name, email, password, gender, dob,
                  city, address, img_path, specialization,
                  experience):
    try:
        doc = session.query(Doctor).get(did)
        if doc:
            user = session.query(Users).get(doc.user_id)
            if name:
                doc.name = name
            if email:
                user.email = email
            if password:
                user.password = password
            if gender:
                doc.gender = gender
            if dob:
                doc.dob = dob
            if city:
                doc.city = city
            if address:
                doc.address = address
            if img_path:
                doc.img_path = img_path
            if specialization:
                doc.specialization = specialization
            if experience:
                doc.experience = experience
            session.commit()
            return {"message": "Doctor updated successfully"}, 200
        else:
            return {"error": "Doctor ID not found"}, 404
    except SQLAlchemyError as ex:
        session.rollback()
        return {"error": str(ex)}, 500
    finally:
        session.close()


def change_online_status(user_id):
    try:
        doc = session.query(Doctor).filter_by(user_id=user_id).first()
        doc.isonline = not doc.isonline
        session.commit()
        return {"message": "status changed"}, 200
    except SQLAlchemyError as ex:
        session.rollback()
        return {"error": str(ex)}, 500
    finally:
        session.close()
