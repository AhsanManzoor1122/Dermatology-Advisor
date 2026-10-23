from sqlalchemy import null
from Model.Disease import Disease
from DBHandler import return_session
from flask import jsonify
import Extentions
from sqlalchemy.orm import exc
from sqlalchemy.exc import SQLAlchemyError
from Controller import UsersController

session = return_session()


def get_disease_details(disease_id):
    try:
        disease_detail = session.query(Disease).filter_by(id=disease_id).first()
        if disease_detail:
            disease = {
                "id": disease_detail.id,
                "name": disease_detail.name,
                "description": disease_detail.description,
                "causes": disease_detail.causes,
                "cure": disease_detail.cure
            }
            return {"data": disease}, 200
        else:
            return {"message": "Disease not found"}, 404

    except Exception as ex:
        return {"error": str(ex)}, 500
    finally:
        session.close()
