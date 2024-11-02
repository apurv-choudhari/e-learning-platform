import mysql.connector
import db_utils as mdb
import os
import subprocess

def setupDB():
    reservationConnection, cursor = mdb.connectDB()
    if not cursor:
        return

    try:
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
        print('Error:', err)
        reservationConnection.rollback()
    finally:
        cursor.close()
        reservationConnection.close()

def main():
    setupDB()
    print("Starting ZyBooks.")
    app = os.path.join(os.path.dirname(__file__), 'app.py')
    subprocess.run(["python", app])

if __name__ == "__main__":
    main()
