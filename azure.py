from flask import Flask, request, render_template
from sqlalchemy import create_engine, inspect, Column, Integer, String, Date, ForeignKey, text
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.orm import declarative_base

Base = declarative_base()

app = Flask(__name__)

# Database setup
engine = create_engine("mysql+pymysql://alyssa:ahi-admin-2023@migrations-hw.mysql.database.azure.com/alyssa",
                         connect_args={'ssl': {'ssl-mode': 'preferred'}},
                         )

Session = sessionmaker(bind=engine)

inspector = inspect(engine)

class Patient(Base):
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    gender = Column(String(10), nullable=False)
    contact_number = Column(String(100))

    records = relationship('MedicalRecord', back_populates='patient')

class MedicalRecord(Base):
    __tablename__ = 'medical_records'

    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patients.id'), nullable=False)
    diagnosis = Column(String(100), nullable=False)
    treatment = Column(String(200))
    admission_date = Column(Date, nullable=False)
    discharge_date = Column(Date)

# Route to get a list of patients
@app.route('/patients')
def get_patients():
    session = Session()
    # Query the database to get a list of patients
    patients = session.execute(text("SELECT * FROM patients")).fetchall()
    medical_records = session.execute(text("SELECT * FROM medical_records")).fetchall()
    # Format and return the patient information
    # patient_info = "\n".join([f"Patient: {patient.first_name} {patient.last_name}" for patient in patients])
    return render_template('index.html', patients=patients, medical_records=medical_records)

# Route to get a list of medical records
@app.route('/medical_records')
def get_medical_records():
    # Query the database to get a list of medical records
    medical_records = engine.execute("SELECT * FROM medical_records").fetchall()
    
    # Format and return the medical record information
    record_info = "\n".join([f"Medical Record: Patient ID {record.patient_id}, Diagnosis: {record.diagnosis}" for record in medical_records])
    return record_info

if __name__ == '__main__':
    app.run(debug=True, port=5005)





# from sqlalchemy import create_engine, inspect, Column, Integer, String, Date, ForeignKey
# from sqlalchemy.orm import relationship
# from sqlalchemy.orm import declarative_base
# from flask import Flask, request
# import os

# Base = declarative_base()

# app = Flask(__name__)

# @app.route('/')
# def patients():
#     return 'patients'

# class Patient(Base):
#     __tablename__ = 'patients'

#     id = Column(Integer, primary_key=True)
#     first_name = Column(String(50), nullable=False)
#     last_name = Column(String(50), nullable=False)
#     date_of_birth = Column(Date, nullable=False)
#     gender = Column(String(10), nullable=False)
#     contact_number = Column(String(100))

#     records = relationship('MedicalRecord', back_populates='patient')

# class MedicalRecord(Base):
#     __tablename__ = 'medical_records'

#     id = Column(Integer, primary_key=True)
#     patient_id = Column(Integer, ForeignKey('patients.id'), nullable=False)
#     diagnosis = Column(String(100), nullable=False)
#     treatment = Column(String(200))
#     admission_date = Column(Date, nullable=False)
#     discharge_date = Column(Date)

# DATABASE_URL = "mysql+mysqlconnector://alyssa:ahi-admin-2023@migrations-hw.mysql.database.azure.com/alyssa"
# engine = create_engine(DATABASE_URL)

# inspector = inspect(engine)
# inspector.get_table_names() 

# if __name__ == '__main__':
#     app.run(debug=True, port=5005)







# """

# pip install sqlalchemy alembic mysql-connector-python pymysql

# """

# ## Part 1 - Define SQLAlchemy models for patients and their medical records:
# ### this file below could always be called db_schema.py or something similar

# from sqlalchemy import create_engine, inspect, Column, Integer, String, Date, ForeignKey
# from sqlalchemy.orm import relationship
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import declarative_base

# Base = declarative_base()

# class Patient(Base):
#     __tablename__ = 'patients'

#     id = Column(Integer, primary_key=True)
#     first_name = Column(String(50), nullable=False)
#     last_name = Column(String(50), nullable=False)
#     date_of_birth = Column(Date, nullable=False)
#     gender = Column(String(10), nullable=False)
#     contact_number = Column(String(15))

#     records = relationship('MedicalRecord', back_populates='patient')

# class MedicalRecord(Base):
#     __tablename__ = 'medical_records'

#     id = Column(Integer, primary_key=True)
#     patient_id = Column(Integer, ForeignKey('patients.id'), nullable=False)
#     diagnosis = Column(String(100), nullable=False)
#     treatment = Column(String(200))
#     admission_date = Column(Date, nullable=False)
#     discharge_date = Column(Date)

#     patient = relationship('Patient', back_populates='records')


# ### Part 2 - initial sqlalchemy-engine to connect to db:

# engine = create_engine("mysql+pymysql://alyssa:ahi-admin-2023@migrations-hw.mysql.database.azure.com/alyssa",
#                          connect_args={'ssl': {'ssl-mode': 'preferred'}},
#                          )

# ## Test connection

# inspector = inspect(engine)
# inspector.get_table_names()


# ### Part 3 - create the tables using sqlalchemy models, with no raw SQL required:

# Base.metadata.create_all(engine)

# ### Running migrations 
# """ these steps are then performed in the termainl, outside of your python code

# # 1. alembic init migrations
# ` alembic init migrations `

# 2. edit alembic.ini to point to your database
# ` sqlalchemy.url = mysql+mysqlconnector://username:password@host/database_name `

# 3. edit env.py to point to your models
# `from db_schema import Base`
# `target_metadata = Base.metadata `

# 4. create a migration
# ` alembic revision --autogenerate -m "create tables" `

# 5. run the migration
# ` alembic upgrade head `

# in addition, you can run ` alembic history ` to see the history of migrations
# or you can run with the --sql flag to see the raw SQL that will be executed

# so it could be like:
# ` alembic upgrade head --sql `

# or if you then want to save it:
# ` alembic upgrade head --sql > migration.sql `

# 6. check the database

# 7. roll back: To roll back a migration in Alembic, you can use the downgrade command. 
# The downgrade command allows you to revert the database schema to a previous 
# migration version. Here's how you can use it:

# `alembic downgrade <target_revision>` 

# or if you want to roll back to the previous version, you can use the -1 flag:
# `alembic downgrade -1`
 

# """




