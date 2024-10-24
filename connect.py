import mysql.connector
from mysql.connector import errorcode
import manageDB as mdb
import os


# Database Credentials
# DBMS_USER
# DBMS_PASS

try:
    reservationConnection = mysql.connector.connect(
        user=os.getenv('DBMS_USER'),
        password=os.getenv('DBMS_PASS'), 
        host='classdb2.csc.ncsu.edu',
        database=os.getenv('DBMS_USER'))
    print("Connect Successful.\n")
    mdb.createDB(reservationConnection)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR: 
        print('Invalid credentials')
    elif err.errno == errorcode.ER_BAD_DB_ERROR: 
        print('Database not found')
    else:
        print('Cannot connect to database:',err)
else:
    #Execute database operations... 
    reservationConnection.close()