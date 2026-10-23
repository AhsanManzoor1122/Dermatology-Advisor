
from flask import Flask,jsonify,request
from sqlalchemy.exc import SQLAlchemyError

import DBHandler
from DBHandler import return_session
from Controller import UsersController, DoctorController, PatientController, CaseController
from Controller import DiseaseController
import Extentions

app = Flask(__name__)

session = return_session()


########### PATIENT ##############
@app.route('/hello', methods=['GET'])
def hello():
    return {"message": 'Hellow World'}


@app.route('/app/signup', methods=['POST'])
def signup_patient():
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        gender = request.form.get('gender')
        city = request.form.get('city')

        if Extentions.email_exists(email=email, role='P'):
            return {"message": "Email already exists"}, 400

        response, status = UsersController.sign_up_patient(name, email, password, gender, city)
        return response, status
    except Exception as ex:
        return {"error": str(ex)}, 500


@app.route('/app/login', methods=['PUT'])
def app_login():
    try:
        email = request.form.get('email')
        password = request.form.get('password')
        response, status = UsersController.login_user(email, password)
        return response, status
    except Exception as ex:
        return {"error": str(ex)}, 500


@app.route('/app/logout/<int:user_id>', methods=['PUT'])
def logoutUser(user_id):
    try:
        response = UsersController.logout_user(user_id)
        return jsonify({"message": response})
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500


@app.route('/app/patient/setCase', methods=['POST'])
async def setCase():
    try:
        user_id = request.form.get('user_id')
        img_path = ''
        if request.files['img']:
            img_path = await Extentions.save_image(request.files['img'])

        disease_id = 1

        response, status = CaseController.set_case(user_id=user_id, disease_id=disease_id, img_path=img_path)
        return response, status
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500


@app.route('/app/patient/getPatientCases/<int:user_id>', methods=['GET'])
def get_patient_cases_route(user_id):
    try:
        response, status = CaseController.get_cases(user_id)
        return jsonify(response), status
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500


@app.route('/app/patient/getPatient/<int:user_id>', methods=['GET'])
def getPatient(user_id):
    try:
        response = PatientController.get_patient(user_id)
        return jsonify(response)
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500


@app.route('/app/patient/updatePatient/<int:user_id>', methods=['PUT'])
async def updatePatient(user_id):
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        gender = request.form.get('gender')
        contact = request.form.get('contact')
        dob = request.form.get('dob')
        city = request.form.get('city')
        address = request.form.get('address')
        img_path = ''
        if request.files.get('img'):
            img_path = await Extentions.save_image(request.files['img'])

        response = PatientController.update_patient(user_id=user_id, name=name, email=email, password=password,
                                                    gender=gender, contact=contact, dob=dob, city=city,
                                                    address=address, img_path=img_path)
        print(name, email, password, gender, contact, dob, city, address, img_path)
        return jsonify(response)
    except SQLAlchemyError as ex:
        return jsonify({"error": str(ex)}), 500
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

@app.route('/app/patient/getDiseaseDetail/<int:disease_id>', methods=['GET'])
def getDiseaseDetail(disease_id):
    try:
        response = DiseaseController.get_disease_details(disease_id=disease_id)
        return jsonify(response)
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500


@app.route('/app/patient/chatWithDoctor', methods=['POST'])
def chatWithDoctor():
    try:
        k = 0
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500


##### ADMIN #######
# AddDoctor
@app.route('/admin/addDoctor', methods=['POST'])
async def addDoctor():
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        if Extentions.email_exists(email=email, role='D'):
            return jsonify({"warning": "Email already exists"}), 400
        gender = request.form.get('gender')
        dob = request.form.get('dob')
        city = request.form.get('city')
        address = request.form.get('address')
        img_path = ''
        if request.files['img']:
            img_path = await Extentions.save_image(request.files['img'])
        specialization = request.form.get('specialization')
        experience = request.form.get('experience')
        is_online = request.form.get('isonline')
        session = request.form.get('session')
        response = await DoctorController.add_doctor(name, email, password, gender, dob,
                                                     city, address, img_path, specialization,
                                                     experience, is_online, session)
        return jsonify({"message": response}), 200
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500


@app.route('/admin/getAllDoctor', methods=['GET'])
def getAllDoctor():
    try:
        response = DoctorController.get_all_doctor()
        return jsonify(response)
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500


@app.route('/admin/getDoctor/<int:user_id>', methods=['GET'])
def getDoctor(user_id):
    try:
        response = DoctorController.get_doctor(user_id)
        return jsonify(response)
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500


@app.route('/admin/updateDoctor/<int:id>', methods=['POST'])
def updateDoctor(id):
    data = request.form
    name = data.get('name')
    email = data.get('email')
    gender = data.get('gender')
    dob = data.get('dob')
    city = data.get('city')
    adress = data.get('adress')
    if 'img' in request.files['img']:
        img_path = Extentions.save_image(request.files['img'])
    else:
        img_path = ''
    specialization = data.get('specialization')
    experience = data.get('experience')
    isonline = data.get('isonline')
    password = data.get('password')
    response = DoctorController.update_doctor(id, name, email, gender, dob,
                                              city, adress, img_path, specialization,
                                              experience, isonline, password)
    UsersController.update_auth(email, password)
    return jsonify(response)


###############################################################################

############# DOCTOR ##################
@app.route('/app/doctor/changeOnlineStatus/<int:user_id>', methods=['PUT'])
def changeOnlineStatus(user_id):
    try:
        response = DoctorController.change_online_status(user_id)
        return jsonify(response), 200
    except Exception as ex:
        return {"error": str(ex)}, 500


#############################################################################


@app.route('/addUser', methods=['POST'])
async def addUser():
    try:
        data = request.form
        email = data.get('email')
        password = data.get('password')
        role = data.get('role')
        user_id, status_code = await UsersController.add_user(email, password, role)
        return jsonify(user_id["user_id"]), status_code
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500


@app.route('/getAllAuth', methods=['GET'])
def getAllAuth():
    response = UsersController.getAllAuth()
    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
