#GCP
from flask import Flask, request, render_template
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
# from dotenv import load_dotenv
# from models import Patient # Assuming you have SQLAlchemy models defined

app = Flask(__name__)

# SQLAlchemy setup with client-side connection pool 
my_connection = 'mysql+pymysql://root:ahi-admin-2023@34.148.90.112/alyssa'
engine = create_engine(my_connection, pool_size=5, max_overflow=10)
Session = sessionmaker(bind=engine)

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

#text('SELECT * FROM patients')
# # GCP type 2
# from flask import Flask, request, jsonify
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from dotenv import load_dotenv
# # from models import Patient # Assuming you have SQLAlchemy models defined

# app = Flask(__name__)

# # SQLAlchemy setup with client-side connection pool 
# db_uri = "mysql+pymysql://root:ahi-admin-2023@34.148.90.112/alyssa"
# engine = create_engine(db_uri, pool_size=5, max_overflow=10)
# Session = sessionmaker(bind=engine)

# @app.route('/get_patient/<int:patient_id>', methods=['GET'])
# def get_patient(patient_id):
#     session = Session()
#     # patient = session.query(Patient).filter_by(id=patient_id).first()
#     result = session.execute("SELECT * FROM patients WHERE id=:patient_id", {"patient_id": patient_id})
#     patient = result.fetchone()
#     session.close()

#     if patient:
#         return jsonify({"patient": {"id": patient.id, "first_name": patient.first_name, "last_name": patient.last_name}})
#     else:
#         return jsonify({"message": "Patient not found"}), 404

# # GC SQL type
# from flask import Flask
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from dotenv import load_dotenv

# load_dotenv()
# db_route = os.getenv("DB_ROUTE") 

# app = Flask(__name__)

# # Server-side connection pool setup (Google Cloud SQL) 
# cloud_sql_connection = create_engine(db_route)
# Session = sessionmaker(bind=cloud_sql_connection)

# @app.route('/get_patient/<patient_id>')
# def get_patient(patient_id):
#     session = Session()
#     patient = session.execute("SELECT * FROM patients WHERE id=:patient_id", {"patient_id": patient_id}).fetchone()
#     session.close()
#     return f"Patient: {patient}"