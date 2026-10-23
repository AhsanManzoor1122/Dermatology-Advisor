import os

from werkzeug.utils import secure_filename
from DBHandler import return_session
from rout import  app
from Model.Users import Users

session = return_session()

UPLOAD_FOLDER = r'C:\Users\Asi Shaiq\Desktop\FYP\ProfImages'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# try:

# except Exception as ex:
#   session.rollback()
#  return {"error": str(ex)}, 500
# finally:
#   session.rollback()
def email_exists(email, role):
    existing_doctor = session.query(Users).filter_by(email=email, role=role).first()
    session.close()
    return existing_doctor is not None


def allowed_file(filename):
    # Check if the file extension is allowed
    ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


async def save_image(file):
    # Save the uploaded file to the specified folder
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        return filepath
    else:
        raise ValueError("Invalid file or file extension not allowed")
