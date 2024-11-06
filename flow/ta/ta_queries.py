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
        cursor.execute(query, (ta_id))
        return cursor.fetchone()
    finally:
        cursor.close()
        conn.close()

def get_students(course_id):
    conn, cursor = connectDB()
    try:
        query = "SELECT stud_id FROM enroll WHERE course_id = %s"
        cursor.execute(query, (course_id))
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

def get_textbook_id(course_id):
    conn, cursor = connectDB()
    try:
        query = "SELECT textbook_id FROM course WHERE course_id = %s"
        cursor.execute(query, (course_id))
        return cursor.fetchone()
    finally:
        cursor.close()
        conn.close()

def get_textbook_id_for_ta(user_id, course_id):
    conn, cursor = connectDB()
    try:
        query = """
            SELECT course.textbook_id FROM teaching_assistant
            JOIN course ON teaching_assistant.course_id = course.course_id
            WHERE teaching_assistant.ta_id = %s AND teaching_assistant.course_id = %s
        """
        cursor.execute(query, (user_id, course_id))
        return cursor.fetchone()
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
