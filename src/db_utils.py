import mysql.connector
from mysql.connector import Error
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SQL_DIR = BASE_DIR / "sql"
IMAGE_DIR = SQL_DIR / "images"
db_setup_path = SQL_DIR / "db_setup.sql"
db_populate_path = SQL_DIR / "populate_data.sql"

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

def insert_images(cursor):
    image_data = [
        (101, 'chap02', 'Sec02', 'Block01', 1, IMAGE_DIR / 'sample1.png', 'Sample image for DBMS content'),
        (102, 'chap02', 'Sec02', 'Block01', 1, IMAGE_DIR / 'sample2.png', 'Sample image for SDLC content')
    ]
    
    insert_query = """
    INSERT INTO image (textbook_id, chapter_id, section_id, block_id, image_id, image_content, alt_text)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    
    for data in image_data:
        textbook_id, chapter_id, section_id, block_id, image_id, image_path, alt_text = data
        try:
            with open(image_path, 'rb') as img_file:
                img_content = img_file.read()
            cursor.execute(insert_query, (textbook_id, chapter_id, section_id, block_id, image_id, img_content, alt_text))
        except Error as e:
            print(f"Error inserting image {image_path.name}: {e}")
            return False
    print("Images inserted successfully.")
    return True
