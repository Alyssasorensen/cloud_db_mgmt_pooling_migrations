from flask import Flask, render_template
from sqlalchemy import create_engine, text  # Import 'text' for executing raw SQL queries
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)

# Database connection settings from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")

# Connection string
conn_string = (
    f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
    f"?charset={DB_CHARSET}"
)

# Database connection settings
db_engine = create_engine(conn_string, echo=False)

@app.route('/')
def index():
    # Create a database connection
    connection = db_engine.connect()

    # Fetch patients and medical records using SQLAlchemy
    patients_query = text("SELECT * FROM patients")
    medical_records_query = text("SELECT * FROM medical_records")

    patients = connection.execute(patients_query).fetchall()
    medical_records = connection.execute(medical_records_query).fetchall()

    # Close the connection
    connection.close()
    
    return render_template('index.html', patients=patients, medical_records=medical_records)

if __name__ == '__main__':
    app.run(debug=True)

print("Fake data insertion complete!")