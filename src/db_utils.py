from errno import errorcode
from aifc import Error
import mysql.connector
from pathlib import Path
import os
from dotenv import load_dotenv
from mysql.connector import errorcode

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
SQL_DIR = BASE_DIR / "sql"
IMAGE_DIR = SQL_DIR / "images"
db_setup_path = SQL_DIR / "db_setup.sql"
db_populate_path = SQL_DIR / "populate_data.sql"

user = os.getenv('DBMS_USER')
password = os.getenv('DBMS_PASS')
host = 'classdb2.csc.ncsu.edu'
database = os.getenv('DBMS_USER')

def connectDB():
    try:
        reservationConnection = mysql.connector.connect(
            user=user,
            password=password,
            host=host,
            database=database
        )
        # print("DB Connect Successful.\n")
        cursor = reservationConnection.cursor()
        return reservationConnection, cursor
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Invalid credentials')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print('Database not found')
        else:
            print('Cannot connect to database:', err)
        return None, None

def executeSQL(cursor, file):
    try:
        with open(file, 'r') as file:
            sql_script = file.read()
            sql_commands = sql_script.split(';')
            for command in sql_commands:
                command = command.strip()
                if command:
                    cursor.execute(command)
    except Error as e:
        print(f"An error occurred: {e}")
        current_filename = Path(__file__).name
        print(f"Error executing SQL from {file} in {current_filename}: {e}")
        return False
    return True

def createDB(cursor):
    return executeSQL(cursor, db_setup_path)

def populateDB(cursor):
    return executeSQL(cursor, db_populate_path)

def clearAll(cursor):
    try:
        cursor.execute("SHOW TABLES")
        tables_to_drop = cursor.fetchall()
        table_names = [table[0] for table in tables_to_drop]
        print("Tables to drop:", table_names)
        cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
        for table in table_names:
            cursor.execute(f"DROP TABLE IF EXISTS {table};")
        cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")
    except Error as e:
        print(f"An error occurred: {e}")
        return False
    return True
