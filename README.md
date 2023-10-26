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

### **Changing connection pool settings like max_connections and connect_timeout for an Azure MySQL Database is done by configuring the database server settings within the Azure portal. Here's how you can change these settings directly in Azure:**

1. Sign in to the Azure portal (https://portal.azure.com).

2. Locate the MySQL Database:

    In the Azure portal, navigate to your Azure MySQL Database.

3. Configure Connection Pool Settings:

    a. On the left-hand menu, under "Settings," click on "Connection security."

    b. You will see options for configuring connection pool settings. Specifically, you can configure these settings:

        Max Connections: This setting defines the maximum number of allowed concurrent connections to your database. You can adjust this based on your needs. For our database input "20."

        Connection Timeout: This setting defines the maximum time a connection request is allowed to wait for a connection to be available. It's specified in seconds. For our database input "3."

4. Save Changes:

    Make the desired changes to max_connections and connect_timeout.

5. Apply Configuration:

    Save your changes. Depending on the Azure portal interface, you might need to click an "Apply" or "Save" button to confirm your configuration changes.

6. Review and Test:

    After making the changes, monitor the performance of your application to ensure that the adjusted connection pool settings meet your requirements.

## **Describe the Database Schema Structure and Rationale**

This is a database schema for storing information about patients and their medical records using SQLAlchemy.

### **Tables:**

**Patients (patients table):**

id: An auto-incremented integer field serving as the primary key.

first_name: A string field (up to 50 characters) representing the patient's first name.

last_name: A string field (up to 50 characters) representing the patient's last name.

date_of_birth: A date field for the patient's date of birth.

gender: A string field (up to 10 characters) representing the patient's gender.

contact_number: A string field (up to 15 characters) for the patient's contact number. This field is nullable, meaning it's not required.

**Medical Records (medical_records table):**

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

**Rationale for some of the design choices:**

Patients Table: This table stores information about patients, including their personal details (name, date of birth, gender) and contact information. The design allows for the management of patients' basic information.

Medical Records Table: This table is associated with patients through a foreign key relationship. It stores details of medical records, including diagnosis, treatment, admission date, and discharge date. The design allows for the tracking of patients' medical history and treatment.

Relationship: The use of a foreign key relationship between the patients and medical_records tables ensures that each medical record is associated with a specific patient, enabling the database to maintain data integrity and link medical records to the corresponding patient.

This schema is a starting point, and additional tables or fields could be added to support more comprehensive medical record management, such as healthcare providers, appointments, or billing information. The schema's simplicity makes it suitable for small-scale applications, but more complexity may be required for larger healthcare systems.

## **Steps and Challenges Encountered During the Database Migration Process**

### **Steps:**

1. Initialize Alembic for migrations:

```
alembic init migrations
```

2. Edit the alembic.ini file to point to your database:
```
sqlalchemy.url = mysql+mysqlconnector://username:password@host/database_name
```

3. In the env.py file, specify where your database models are located:

```
from db_schema import Base
target_metadata = Base.metadata
```

4. Create a migration: 

```
alembic revision --autogenerate -m "create tables"
```

5. Apply the migration:

```
alembic upgrade head
```

6. To view the migration history or see the raw SQL executed during migration, you can use the following commands:

    View history:

    ```
    alembic history
    ```

    View SQL:

    ```
    alembic upgrade head --sql
    ```

    Save SQL to a file:

    ```
    alembic upgrade head --sql > migration.sql
    ```

7. Check your database to confirm the changes.

8. Roll back (if needed):

To revert to a previous migration version, use the downgrade command. Here are two examples:

Roll back to a specifc target revision:

```
alembic downgrade <target_revision>
```

Roll back to the previous version:

```
alembic downgrade -1
```

### **Challenges:**

I did not experience any challenges for the database migration process. However, when I attempted to access my Flask application, I faced a few difficulties. The first hurdle was configuring the development environment, ensuring that Flask and its dependencies were correctly installed. This involved managing virtual environments and handling Python package versions.
Furthermore, I encountered challenges related to routing and URL configurations within my Flask application. Correctly defining routes and ensuring that they match the expected URLs made it tricky especially when using Azure and GCP. Debugging errors or misconfigurations in route handlers took some time before finally getting it correct. 
Deployment was another aspect that presented some difficulties. When deploying the Flask application, operational errors and attribute errors kept appearing. The reason for this was because the data was not properly inserted into the tables in MySQL Workbench. Therefore, there was no data to display in the Flask application. Once the data was inserted correctly, I configured the app route correctly so that it corresponded to my HTML file, and then I was able to view the tables with data. 

