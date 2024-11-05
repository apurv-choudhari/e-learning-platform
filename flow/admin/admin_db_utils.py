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
            return True
            
    except Exception as e:
        db_connection.rollback()
        print("Error:", e)
        return False
    finally:
        cursor.close()
        db_connection.close()


def insert_textbook(title, textbook_id, user_id):
    db_connection, cursor = connectDB()
    
    try:
        cursor.execute("""
            INSERT INTO textbook (textbook_id, title, created_by, updated_by)
            VALUES (%s, %s, %s, %s)
        """, (textbook_id, title, user_id, user_id))
        
        db_connection.commit()
        print("New E-textbook created successfully.")
        return True
    except Exception as e:
        db_connection.rollback()
        print("Error creating textbook:", e)
        return False
    finally:
        cursor.close()
        db_connection.close()

def insert_chapter(user_id, textbook_id, chapter_id, chapter_title):
    db_connection, cursor = connectDB()
    
    try:
        cursor.execute("""
            INSERT INTO chapter (textbook_id, chapter_id, title, is_hidden, created_by, updated_by)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (textbook_id, chapter_id, chapter_title, False, user_id, user_id))
        
        db_connection.commit()
        print("New chapter created successfully.")
        return True
    except Exception as e:
        db_connection.rollback()
        print("Error creating chapter:", e)
        return False
    finally:
        cursor.close()
        db_connection.close()

def insert_section(textbook_id, chapter_id, section_id, section_title, user_id):
    db_connection, cursor = connectDB()
    
    try:
        cursor.execute("""
            INSERT INTO section (textbook_id, chapter_id, section_id, title, is_hidden, created_by, updated_by)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (textbook_id, chapter_id, section_id, section_title, False, user_id, user_id))
        
        db_connection.commit()
        print("New section created successfully.")
        return True
    except Exception as e:
        db_connection.rollback()
        print("Error creating section:", e)
        return False
    finally:
        cursor.close()
        db_connection.close()

def insert_content_block(textbook_id, chapter_id, section_id, block_id, is_type, user_id):
    db_connection, cursor = connectDB()
    
    try:
        cursor.execute("""
            INSERT INTO content_block (textbook_id, chapter_id, section_id, block_id, is_type, is_hidden, created_by, updated_by)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (textbook_id, chapter_id, section_id, block_id, is_type, False, user_id, user_id))
        
        db_connection.commit()
        print("New content block created successfully.")
        return True
    except Exception as e:
        db_connection.rollback()
        print("Error creating content block:", e)
        return False
    finally:
        cursor.close()
        db_connection.close()

def insert_text_content(textbook_id, chapter_id, section_id, block_id, text_id, text_content):
    db_connection, cursor = connectDB()
    
    try:
        cursor.execute("""
            INSERT INTO text (textbook_id, chapter_id, section_id, block_id, text_id, text_content)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (textbook_id, chapter_id, section_id, block_id, text_id, text_content))
        
        db_connection.commit()
        return True
    except Exception as e:
        db_connection.rollback()
        print("Error adding text:", e)
        return False
    finally:
        cursor.close()
        db_connection.close()

def insert_image_content(textbook_id, chapter_id, section_id, block_id, image_id, image_content, alt_text):
    db_connection, cursor = connectDB()
    
    try:
        cursor.execute("""
            INSERT INTO image (textbook_id, chapter_id, section_id, block_id, image_id, image_content, alt_text)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (textbook_id, chapter_id, section_id, block_id, image_id, image_content, alt_text))
        
        db_connection.commit()
        return True
    except Exception as e:
        db_connection.rollback()
        print("Error adding image:", e)
        return False
    finally:
        cursor.close()
        db_connection.close()

def insert_activity(textbook_id, chapter_id, section_id, block_id, activity_id, user_id):
    db_connection, cursor = connectDB()
    
    try:
        cursor.execute("""
            INSERT INTO activity (textbook_id, chapter_id, section_id, block_id, activity_id, is_hidden, created_by, updated_by)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (textbook_id, chapter_id, section_id, block_id, activity_id, False, user_id, user_id))
        
        db_connection.commit()
        return True
    except Exception as e:
        db_connection.rollback()
        print("Error adding activity:", e)
        return False
    finally:
        cursor.close()
        db_connection.close()

def insert_question(textbook_id, chapter_id, section_id, block_id, activity_id, question_id, question_text, options, correct_answer, user_id):
    db_connection, cursor = connectDB()
    
    try:
        cursor.execute("""
            INSERT INTO question (
                textbook_id, chapter_id, section_id, block_id, activity_id, question_id, question_text,
                option1, option1_explanation, option2, option2_explanation,
                option3, option3_explanation, option4, option4_explanation, correct_answer, is_hidden, created_by, updated_by
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            textbook_id, chapter_id, section_id, block_id, activity_id, question_id, question_text,
            options[0][0], options[0][1], options[1][0], options[1][1],
            options[2][0], options[2][1], options[3][0], options[3][1], correct_answer, False, user_id, user_id
        ))
        
        db_connection.commit()
        return True
    except Exception as e:
        db_connection.rollback()
        print("Error adding question:", e)
        return False
    finally:
        cursor.close()
        db_connection.close()

from src.db_utils import connectDB

def get_next_text_id(textbook_id, chapter_id, section_id, block_id):
    db_connection, cursor = connectDB()
    try:
        cursor.execute("""
            SELECT COALESCE(MAX(text_id), 0) + 1 FROM text
            WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s AND block_id = %s
        """, (textbook_id, chapter_id, section_id, block_id))
        next_text_id = cursor.fetchone()[0]
        return next_text_id
    finally:
        cursor.close()
        db_connection.close()

def get_next_image_id(textbook_id, chapter_id, section_id, block_id):
    db_connection, cursor = connectDB()
    try:
        cursor.execute("""
            SELECT COALESCE(MAX(image_id), 0) + 1 FROM image
            WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s AND block_id = %s
        """, (textbook_id, chapter_id, section_id, block_id))
        next_image_id = cursor.fetchone()[0]
        return next_image_id
    finally:
        cursor.close()
        db_connection.close()
