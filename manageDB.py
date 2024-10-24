
from mysql.connector import Error
def createDB(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            age INT NOT NULL
        )
        ''')
        cursor.execute('''
        INSERT INTO users (name, age)
        VALUES (%s, %s)
        ''', ("Alice", 30))

        # Commit the transaction to save the data in the database
        conn.commit()

        # Retrieve data from the table
        cursor.execute('SELECT * FROM users')
        rows = cursor.fetchall()

        # Display the retrieved data
        for row in rows:
            print(row)

        # Close the cursor and connection
        cursor.close()

    except Error as e:
        print(f"An error occurred: {e}")
