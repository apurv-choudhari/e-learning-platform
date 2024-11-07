import sys
import mysql.connector
import db_utils as mdb
import os
import subprocess

plugin_path = os.path.join(os.path.dirname(__file__), "plugin")
os.environ["LD_LIBRARY_PATH"] = plugin_path
BASE_DIR = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
PARENT_DIR = os.path.dirname(BASE_DIR)
sys.path.insert(0, PARENT_DIR)

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
    app = os.path.join(os.path.dirname(__file__), 'src/app.py')

    if "run_app" not in sys.argv:
        print("Running app.py in a subprocess.")
        subprocess.run([sys.executable, app, "run_app"])  # Pass the flag to indicate it's a subprocess.
        return


if __name__ == "__main__":
    main()
