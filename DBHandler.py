import sqlalchemy as sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
class DBHandler:
    Base = declarative_base()
    def __init__(self, server, database, username, password):
        connection_string = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server'
        self.engine = create_engine(connection_string, echo=True)
        self.Session = sessionmaker(bind=self.engine)
def return_session():
    server = r'DESKTOP-5BQEVSV\SQLEXPRESS'
    database = 'DermaAdvisor'
    username = 'sa'
    password = 123
    db_handler = DBHandler(server=server, database=database, username=username, password=password)
    return db_handler.Session()


def check_database_connection():
    try:
        server = r'DESKTOP-5BQEVSV\SQLEXPRESS'
        database = 'DermaAdvisor'
        username = 'sa'
        password = 123
        db_handler = DBHandler(server=server, database=database, username=username, password=password)
        db_handler.engine.connect()
        print("Database connection successful.")
    except Exception as e:
        print(f"Error connecting to the database: {str(e)}")
        exit()

check_database_connection()
