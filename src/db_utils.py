
from mysql.connector import Error
import os

db_setup_path = os.path.join(os.path.dirname(__file__), '..', 'sql', 'db_setup.sql')
db_populate_path = os.path.join(os.path.dirname(__file__), '..', 'sql', 'user_populate_data.sql')

def executeSQL(cursor, file):
    try:
        with open(file, 'r') as file:
            sql_script = file.read()
            sql_commands = sql_script.split(';')
            for command in sql_commands:
                command = command.strip()
                cursor.execute(command)
    except Error as e:
        print(f"An error occurred: {e}")
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
        print(table_names)
        cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
        drop_query = f"DROP TABLE IF EXISTS {', '.join(table_names)};"
        cursor.execute(drop_query)
    except Error as e:
        print(f"An error occurred: {e}")
        return False
    return True
