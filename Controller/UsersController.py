from Model.Patient import Patient
from Model.Users import Users
from DBHandler import return_session
import DBHandler
from DBHandler import DBHandler
from flask import jsonify
from sqlalchemy.exc import SQLAlchemyError

session = return_session()


def sign_up_patient(name, email, password, gender, city):
    try:
        entity = Users(session=0, name=name, email=email, password=password, gender=gender, city=city, role='p')
        session.add(entity)
        session.commit()
        patient = Patient(user_id=entity.id)
        session.add(patient)
        session.commit()
        return {"response": "Patient Signup successful"}, 200
    except Exception as ex:
        session.rollback()
        return {"error": str(ex)}, 500
    finally:
        session.close()


def login_user(email, password):
    try:
        user = session.query(Users).filter_by(email=email, password=password).first()
        if user:
            user.session = 1
            session.commit()
            return {"isValid": 1, "user_id": user.id, "user_role": user.role}, 200
        else:
            return {"isValid": 0}, 400
    except Exception as ex:
        session.rollback()
        return {"error": str(ex)}, 500
    finally:
        session.close()


def logout_user(user_id):
    try:
        user = session.query(Users).get(user_id)
        if user:
            user.session = 0
            session.commit()
            return {"message": "user logged out"}, 200
        else:
            return {"error": "user not found"}, 404
    except SQLAlchemyError as ex:
        session.rollback()
        return {"error": str(ex)}, 500
    finally:
        session.close()


def getAllAuth():
    try:
        session = DBHandler.return_session()
        entities = session.query(Users).all()
        auth_list = [{"email": entity.email, "password": entity.password, "role": entity.role} for entity in entities]
        return {"data": auth_list}, 200
    except Exception as ex:
        return {"error": str(ex)}, 500


def update_auth(email, password):
    try:
        auth = session.query(Users).get(email)
        if auth:
            auth.email = email
            auth.password = password
            session.commit()
            session.close()
            return {"message": "Authentication updated successfully"}, 200
        else:
            return {"error": "Authentication not found"}, 404
    except SQLAlchemyError as ex:
        session.rollback()
        session.close()
        return {"error": str(ex)}, 500
