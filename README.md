# cloud_db_mgmt_pooling_migrations
## **HHA 504 Homework Assignment 4C** 

*Acquire hands-on expertise in overseeing a cloud-hosted MySQL database, with an emphasis on executing connection pooling and executing database migrations. This task will involve working with both Azure and Google Cloud Platform (GCP).* 

## **The Setup and Configuration of Connection Pooling for Azure and GCP databases**

### **Creating a MySQL Database Instance on Azure:**

1. Sign in to Azure: Go to the Azure portal and sign in with your Azure account.

2. Create a New Resource: Click on the "+ Create a resource" button and search for "Azure Database for MySQL." Select this option.

3. Configure Database Settings: Fill out the necessary information, including the server name, username, and password.

4. Choose Pricing Tier: Select the pricing tier that suits your needs and budget. Azure offers various performance and pricing options.

5. Network and Security Settings: Configure the network and firewall settings to control access to your MySQL instance.

6. Review and Create: Review your settings, and if everything looks good, click the "Create" button to deploy the MySQL database instance.

7. Access Your Database: Once the deployment is complete, you can access your MySQL instance using tools like MySQL Workbench or the Azure portal.

8. After the instance was created, I added a database named "Alyssa."

### **Creating a MySQL Database Instance on Google Cloud Platform (GCP):**

1. Sign in to GCP: Go to the Google Cloud Console and log in to your GCP account.

2. Create a New Database: In the left-hand menu, navigate to "SQL" under the "Storage" section.

3. Create Instance: Click on the "Create Instance" button to begin the setup.

4. Choose MySQL as the Database Engine: Select MySQL as your database engine.

5. Configure Instance Details: Fill out the instance ID, password, and other configuration details.

6. Choose the Configuration: Select the machine type, storage capacity, and other configuration settings based on your needs.

7. Configure Access: Set up the access control, including IP addresses that are allowed to connect to your MySQL instance.

8. Review and Create: Review your settings, and if they are correct, click the "Create" button to create your MySQL instance.

9. After the instance was created, I added a database named "Alyssa."

10. I then went back to the instance information on GCP, clicked on "Connections" then "Networking" and added a new network by inputting a name and network identifier.    

## **Describe the Database Schema Structure and Rationale**

This is a database schema for storing information about patients and their medical records using SQLAlchemy.

**Tables:**

Patients (patients table):

id: An auto-incremented integer field serving as the primary key.

first_name: A string field (up to 50 characters) representing the patient's first name.

last_name: A string field (up to 50 characters) representing the patient's last name.

date_of_birth: A date field for the patient's date of birth.

gender: A string field (up to 10 characters) representing the patient's gender.

contact_number: A string field (up to 15 characters) for the patient's contact number. This field is nullable, meaning it's not required.

Medical Records (medical_records table):

id: An auto-incremented integer field serving as the primary key.

patient_id: An integer field that serves as a foreign key referencing the id field of the patients table. This establishes a relationship between medical records and patients.

diagnosis: A string field (up to 100 characters) representing the patient's diagnosis.

treatment: A string field (up to 200 characters) representing the patient's treatment.

admission_date: A date field for the date of admission to the medical facility.

discharge_date: A date field for the date of discharge from the medical facility.

**Relationships:**
A one-to-many relationship exists between the patients and medical_records tables. This means that one patient can have multiple medical records, as indicated by the patient_id field in the medical_records table referencing the id field in the patients table.

**Connection to the Database:**
The code specifies a DATABASE_URL that includes the necessary connection details for accessing the MySQL database. It uses the mysql+pymysql dialect for the database URL, which is common for MySQL databases.
It also includes connection parameters like the username (root), password, host, and database name (alyssa).

**Database Creation:**
The Base.metadata.create_all(engine) statement creates the database tables using the SQLAlchemy models defined in the code. This is done without the need for writing raw SQL, as SQLAlchemy handles the schema creation.

**Rationale:**
The database schema appears to be designed for a healthcare management system. The structure is simple, with two main tables: one for patients and another for their medical records. 

Rationale for some of the design choices:
Patients Table: This table stores information about patients, including their personal details (name, date of birth, gender) and contact information. The design allows for the management of patients' basic information.

Medical Records Table: This table is associated with patients through a foreign key relationship. It stores details of medical records, including diagnosis, treatment, admission date, and discharge date. The design allows for the tracking of patients' medical history and treatment.

Relationship: The use of a foreign key relationship between the patients and medical_records tables ensures that each medical record is associated with a specific patient, enabling the database to maintain data integrity and link medical records to the corresponding patient.

This schema is a starting point, and additional tables or fields could be added to support more comprehensive medical record management, such as healthcare providers, appointments, or billing information. The schema's simplicity makes it suitable for small-scale applications, but more complexity may be required for larger healthcare systems.

## **Steps and Challenges Encountered During the Database Migration Process**

## **Screenshots Demonstrating the Flask application's Interaction with Both Databases**

## **If you encounter any errors or challenges, document them thoroughly, providing screenshots, descriptions of your troubleshooting steps, and potential root causes**