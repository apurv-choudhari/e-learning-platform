from db_utils import connectDB

def get_password(user_id, role_no):
    conn, cursor = connectDB()
    try:
        query = "SELECT password FROM user WHERE user_id = %s AND role_no = %s"
        cursor.execute(query, (user_id, role_no))
        return cursor.fetchone()
    finally:
        cursor.close()
        conn.close()

def update_password(user_id, new_password):
    conn, cursor = connectDB()
    try:
        query = "UPDATE user SET password = %s WHERE user_id = %s"
        cursor.execute(query, (new_password, user_id))
        conn.commit()
    finally:
        cursor.close()
        conn.close()

def get_course_id(ta_id):
    conn, cursor = connectDB()
    try:
        query = "SELECT course_id FROM teaching_assistant WHERE ta_id = %s"
        cursor.execute(query, (ta_id,))
        return cursor.fetchone()
    finally:
        cursor.close()
        conn.close()

def get_students(course_id):
    conn, cursor = connectDB()
    try:
        query = "SELECT stud_id FROM enroll WHERE course_id = %s"
        cursor.execute(query, (course_id,))
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

def get_textbook_id(course_id):
    conn, cursor = connectDB()
    try:
        query = "SELECT textbook_id FROM course WHERE course_id = %s"
        cursor.execute(query, (course_id,))
        result = cursor.fetchone()
        return result[0] if result else None
    finally:
        cursor.close()
        conn.close()

def get_textbook_id_for_ta(course_id, user_id):
    conn, cursor = connectDB()
    try:
        query = """
            SELECT course.textbook_id FROM teaching_assistant
            JOIN course ON teaching_assistant.course_id = course.course_id
            WHERE teaching_assistant.ta_id = %s AND teaching_assistant.course_id = %s
        """
        cursor.execute(query, (user_id, course_id))
        result = cursor.fetchone()
        return result[0] if result else None
    finally:
        cursor.close()
        conn.close()

def get_content_block_id(textbook_id, chapter_id, section_id):
    conn, cursor = connectDB()
    try:
        query = """
            SELECT block_id FROM content_block
            WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s
        """
        cursor.execute(query, (textbook_id, chapter_id, section_id))
        return cursor.fetchone()
    finally:
        cursor.close()
        conn.close()
        
def insert_chapter(user_id, course_id, chapter_id, chapter_title):
    try:
        db_connection, cursor = connectDB()
        
        # Query to get the textbook ID based on course_id and user_id (fac_id)
        cursor.execute("""
            SELECT textbook_id
            FROM course
            WHERE course_id = %s
        """, (course_id,))
        
        result = cursor.fetchone()
        if result:
            textbook_id = result[0]
        else:
            print("No textbook found for the given course_id and user_id.")
            return False

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


def insert_section(course_id, chapter_id, section_id, section_title, user_id):
    try:
        db_connection, cursor = connectDB()
        
        cursor.execute("""
            SELECT textbook_id
            FROM course
            WHERE course_id = %s
        """, (course_id,))

        result = cursor.fetchone()

        if result is not None:
            textbook_id = result[0]
            
            # Insert the new section into the section table
            cursor.execute("""
                INSERT INTO section (textbook_id, chapter_id, section_id, title, is_hidden, created_by, updated_by)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (textbook_id, chapter_id, section_id, section_title, False, user_id, user_id))

            db_connection.commit()
            print("New section created successfully.")
            return True
        else:
            print("No textbook found for the given course_id and user_id.")
            return False

    except Exception as e:
        db_connection.rollback()
        print("Error inserting section:", e)
        return False

    finally:
        cursor.close()
        db_connection.close()

def insert_content_block(user_id, course_id, chapter_id, section_id, block_id, is_type):
    try:
        db_connection, cursor = connectDB()
        textbook_id = get_textbook_id(course_id)
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

def hide_activity(user_id, course_id, chapter_id, section_id, block_id):
    print("\nTA: Hide Activity")
    activity_id = input("Provide Activity ID: ")
    try:
        db_connection, cursor = connectDB()
        textbook_id = get_textbook_id_for_ta(course_id, user_id)
        cursor.execute("""
            UPDATE activity
            SET is_hidden = TRUE, updated_by = %s
            WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s AND block_id = %s AND activity_id = %s
        """, (user_id, textbook_id, chapter_id, section_id, block_id, activity_id))
        
        db_connection.commit()
        print("Activity successfully hidden.")
        return True
    except Exception as e:
        db_connection.rollback()
        print("Error hiding activity:", e)
        return False
    finally:
        cursor.close()
        db_connection.close()

def hide_content_block_util(user_id, course_id, chapter_id, section_id, block_id):
    try:
        db_connection, cursor = connectDB()
        textbook_id = get_textbook_id_for_ta(course_id, user_id)

        cursor.execute("""
            UPDATE content_block
            SET is_hidden = TRUE, updated_by = %s
            WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s AND block_id = %s
        """, (user_id, textbook_id, chapter_id, section_id, block_id))
        
        db_connection.commit()
        print("Content block successfully hidden.")
        return True
    except Exception as e:
        db_connection.rollback()
        print("Error hiding content block:", e)
        return False
    finally:
        cursor.close()
        db_connection.close()

def del_content_block(user_id, course_id, chapter_id, section_id, block_id):
    try:
        db_connection, cursor = connectDB()
        textbook_id = get_textbook_id_for_ta(course_id, user_id)
        
        cursor.execute("""
            SELECT u.role_no
            FROM user u
            JOIN content_block cb ON cb.updated_by = u.user_id
            WHERE cb.block_id = %s AND cb.section_id = %s AND cb.chapter_id = %s AND cb.textbook_id = %s AND u.user_id = %s
        """, (block_id, section_id, chapter_id, textbook_id, user_id))
        
        result = cursor.fetchone()
        
        if result is not None:
            role_no = result[0]
            if role_no == 4:
                cursor.execute("""
                    DELETE FROM content_block
                    WHERE block_id = %s AND section_id = %s AND chapter_id = %s AND textbook_id = %s
                """, (block_id, section_id, chapter_id, textbook_id))

                db_connection.commit()
                print("Content block deleted successfully.")
                return True
            else:
                print("User role does not permit deletion of the content block.")
                return False
        else:
            print("Content block not found for the given block_id, section_id, and chapter_id.")
            return False

    except Exception as e:
        print("Error deleting content block:", e)
        return False

    finally:
        cursor.close()
        db_connection.close()