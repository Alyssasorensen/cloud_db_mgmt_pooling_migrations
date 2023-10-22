import os
from dotenv import load_dotenv
from sqlalchemy.orm import declarative_base
from faker import Faker
import random

# Load environment variables
load_dotenv()

# Database connection settings from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")

# Connection string
conn_string = (
    f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
    f"?charset={DB_CHARSET}"
)

Base = declarative_base()

# Create a database engine
db_engine = create_engine(conn_string, echo=False)
fake = Faker()

sample_patients = ['John Smith', 'Jane Doe', 'Taylor Swift', 'Travis Kelce', 
                      'Selena Gomez', 'Mike Candy', 'Wendy Sun', 
                      'Emily Wall', 'Teddy Bear']

def insert_fake_data(engine, num_patients=30, num_medical_records=20): # Noqa: E501
    # Start a connection
    with engine.connect() as connection:
        # Insert fake data into patients
        for _ in range(num_patients):
            first_name = fake.first_name()
            last_name = fake.last_name()
            date_of_birth = fake.date_of_birth(minimum_age=10, maximum_age=90)
            connection.execute(f"INSERT INTO patients (first_name, last_name, date_of_birth) VALUES ('{first_name}', '{last_name}', '{date_of_birth}')") # Noqa: E501

        # Insert sample patients into medical_records
        for patient in sample_patients:
            connection.execute(f"INSERT INTO patients (first_name) VALUES ('{patient}')")
        
        # Insert fake data into medical_records
        for _ in range(medical_records):
            patient_id = random.choice(patient_ids)
            diagnosis = random.choice(diagnosis)
            treatment = random.choice(treatment)
            admission_date = fake.date_between(start_date="-5y", end_date="today")
            discharge_date = fake.date_between(start_date="-5y", end_date="today")
            connection.execute(f"""INSERT INTO medical_records (patient_id, diagnosis, treatment, start_date="-5y", end_date="today", start_date="-5y", end_date="today" ) VALUES ({patient_id}, {diagnosis}, {treatment}, {start_date="-5y", end_date="today"}, {start_date="-5y", end_date="today"}""") # Noqa: E501

if __name__ == "__main__":
    insert_fake_data(db_engine)
    print("Fake data insertion complete!")

@app.route('/')
def index():
    # Fetch patients and medical records using SQLAlchemy
    patients = db_engine.execute("SELECT * FROM patients").fetchall()
    medical_records = db_engine.execute("SELECT * FROM medical_records").fetchall()
    
    return render_template('index.html', patients=patients, medical_records=medical_records)