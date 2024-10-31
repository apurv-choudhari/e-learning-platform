
from mysql.connector import Error
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
print(f"Base Dir:{BASE_DIR}")
SQL_DIR = BASE_DIR / "sql"
db_setup_path = SQL_DIR/"db_setup.sql"
db_populate_path = SQL_DIR/"user_populate_data.sql"


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
        print(table_names)
        cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
        drop_query = f"DROP TABLE IF EXISTS {', '.join(table_names)};"
        cursor.execute(drop_query)
    except Error as e:
        print(f"An error occurred: {e}")
        return False
    return True
