import mysql.connector
from mysql.connector import errorcode
from dotenv import load_dotenv
import db_utils as mdb
import os
import subprocess

load_dotenv()

user=os.getenv('DBMS_USER')
password=os.getenv('DBMS_PASS')
host='classdb2.csc.ncsu.edu'
database=os.getenv('DBMS_USER')
print(f"User:{user}, Password:{password}, Host:{host}, Database:{database}")
# cursor = None

def connectDB():
    print(os.getenv('DBMS_USER'))
    reservationConnection = mysql.connector.connect(
        user=user,
        password=password,
        host=host,
        database=database)
    print("Connect Successful.\n")
    cursor = reservationConnection.cursor()
    return reservationConnection, cursor

def setupDB():
    try:
        reservationConnection, cursor = connectDB()

        if mdb.clearAll(cursor):
            print("Database Cleared.")

        if mdb.createDB(cursor):
            print("Database Creation Successful.")
        else:
            print("Database Creation Failed.")
        
        if mdb.populateDB(cursor):
            print("Database Population Successful.")
        else:
            print("Database Population Failed.")

        reservationConnection.commit()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Invalid credentials')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print('Database not found')
        else:
            print('Cannot connect to database:',err)
    else:
        reservationConnection.close()

def main():
    setupDB()
    print("Starting ZyBooks.")
    app = os.path.join(os.path.dirname(__file__), 'app.py')
    subprocess.run(["python", app])

if __name__ == "__main__":
    main()
