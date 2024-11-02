from src.db_utils import connectDB

def insert_user(user_id, first_name, last_name, email, password, role_no):
    db_connection, cursor = connectDB()
    
    try:
        cursor.execute("SELECT 1 FROM user WHERE user_id = %s", (user_id,))
        user_exists = cursor.fetchone()
        print('user exits:')
        print(user_exists)
        if user_exists:
            print("User ID already exists.")
        else:
            cursor.execute("""
                INSERT INTO user (user_id, email, first_name, last_name, password, role_no)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (user_id, email, first_name, last_name, password, role_no))
            
            cursor.execute("""
                INSERT INTO faculty (fac_id)
                VALUES (%s)
            """, (user_id,))
            
            db_connection.commit()
            print("Faculty account created successfully.")
            
    except Exception as e:
        db_connection.rollback()
        print("Error:", e)
    finally:
        cursor.close()
        db_connection.close()


def insert_textbook():
    print('creating new textbook')
    return False