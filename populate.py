import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
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

my_connection = 'mysql+pymysql://root:ahi-admin-2023@34.148.90.112/alyssa'

# Create a database engine
db_engine = create_engine(my_connection, echo=False)
fake = Faker()

def insert_fake_data(engine, num_patients=30, num_medical_records=20): # Noqa: E501
    # Start a connection
    with engine.connect() as connection:
        # Insert fake data into patients
        for _ in range(num_patients):
            first_name = fake.first_name()
            last_name = fake.last_name()
            date_of_birth = fake.date_of_birth(minimum_age=10, maximum_age=90)
            query = text(f"""INSERT INTO patients (first_name, last_name, date_of_birth, gender) VALUES ('{first_name}', '{last_name}', '{date_of_birth}', 'male')""")
            connection.execute(query) # Noqa: E501

if __name__ == "__main__":
    insert_fake_data(db_engine)
print("Fake data insertion complete!")






from sqlalchemy.sql import text

# ...

def insert_fake_data(engine, num_patients=30, num_medical_records=20):
    with engine.connect() as connection:
        # Insert fake data into patients
        for _ in range(num_patients):
            first_name = fake.first_name()
            last_name = fake.last_name()
            insert_patient = text(
                "INSERT INTO Users (UserName) VALUES (:user_name)"
            )
            connection.execute(insert_patient, user_name=f"{first_name} {last_name}")

        # Insert sample patients into medical_records
        for medical in medical_records:
            insert_sample_patient = text(
                "INSERT INTO Users (UserName) VALUES (:user_name)"
            )
            connection.execute(insert_sample_medical_record, user_name=medical)

        # Insert fake data into medical_records
        for _ in range(num_medical_records):
            patient_id = random.randint(1, num_patients)
            diagnosis = fake.text(max_nb_chars=50)
            treatment = fake.text(max_nb_chars=50)
            admission_date = fake.date_between(start_date="-5y", end_date="today")
            discharge_date = fake.date_between(start_date="-5y", end_date="today")
            insert_medical_record = text(
                "INSERT INTO Orders (OrderDate, UserID) VALUES "
                "(:order_date, :user_id)"
            )
            connection.execute(
                insert_medical_record,
                order_date=admission_date,
                user_id=patient_id,
            )

# Call the function to insert data into the Google Cloud SQL database
insert_fake_data(gcphw4c)
print("Fake data insertion complete!")
