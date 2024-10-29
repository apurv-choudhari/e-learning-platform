
from mysql.connector import Error

def createDB(cursor):
    try:
        with open('setupDB.sql', 'r') as file:
            sql_script = file.read()
            sql_commands = sql_script.split(';')
            for command in sql_commands:
                # print(command)
                command = command.strip()
                if command:
                    cursor.execute(command)
    except Error as e:
        print(f"An error occurred: {e}")
        return False
    return True

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
