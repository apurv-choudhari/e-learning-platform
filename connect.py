import mysql.connector
from mysql.connector import errorcode
try:
    reservationConnection = mysql.connector.connect(
        user='apchoudh',
        password='200537263', host='classdb2.csc.ncsu.edu',
        database='apchoudh')
    print("Connect Successful")
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