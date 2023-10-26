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