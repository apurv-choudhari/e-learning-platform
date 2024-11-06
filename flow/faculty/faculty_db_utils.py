from src.db_utils import connectDB


def get_textbook_id(course_id, user_id):
    try:
        db_connection, cursor = connectDB()
        
        cursor.execute("""
            SELECT textbook_id
            FROM course
            WHERE course_id = %s AND fac_id = %s
        """, (course_id, user_id))

        result = cursor.fetchone()

        if result is not None:
            textbook_id = result[0]
            return textbook_id  
        else:
            print("No textbook found for the given course_id and user_id.")
            return None

    except Exception as e:
        print("Error retrieving textbook ID:", e)
        return None  

    finally:
        cursor.close()
        db_connection.close()

def validate_active_course(course_id):
    try:
        db_connection, cursor = connectDB()
        cursor.execute("""
            SELECT 1
            FROM active_course
            WHERE course_id = %s
        """, (course_id,))
        result = cursor.fetchone()

        if result is not None:
            return True
        else: return False
    except Exception as e:
        print("Error validating active course:", e)
        return False
    finally:
        cursor.close()
        db_connection.close()

def validate_enrollment_course(course_id):
    try:
        db_connection, cursor = connectDB()
        cursor.execute("""
            SELECT 1
            FROM active_course
            WHERE course_id = %s
        """, (course_id,))
        result = cursor.fetchone()

        if result is None:
            return True
        else: return False

    except Exception as e:
        print("Error validating active course:", e)
    finally:
        cursor.close()
        db_connection.close()

def select_courses(faculty_id):
    try:
        db_connection, cursor = connectDB()
        
        # SQL query to select courses associated with a given faculty_id
        query = """
            SELECT course_id, title
            FROM course
            WHERE fac_id = %s
        """
        cursor.execute(query, (faculty_id,))
        
        courses = cursor.fetchall()
        
        return courses

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    
    finally:
        cursor.close()
        db_connection.close()

def update_password(faculty_id, curr_password, new_password, confirm_new_password):
    # Check if new_password and confirm_new_password are the same
    if new_password != confirm_new_password:
        print("New password and confirm password do not match.")
        return False
    
    # Check if new_password is different from current password
    if new_password == curr_password:
        print("New password cannot be the same as the current password.")
        return False
    
    try:
        db_connection, cursor = connectDB()
        
        # SQL query to check if current password is correct
        query_check_password = """
            SELECT password 
            FROM user 
            WHERE user_id = %s
        """
        cursor.execute(query_check_password, (faculty_id,))
        result = cursor.fetchone()
        
        # If no record is found or the current password does not match
        if not result or result[0] != curr_password:
            print("Current password is incorrect.")
            return False

        # SQL query to update password
        query_update_password = """
            UPDATE user
            SET password = %s
            WHERE user_id = %s
        """
        cursor.execute(query_update_password, (new_password, faculty_id))
        
        db_connection.commit()
        print("Password updated successfully.")
        return True

    except Exception as e:
        print(f"An error occurred: {e}")
        return False

    finally:
        cursor.close()
        db_connection.close()

def select_waitlist(course_id): 
    try:
        db_connection, cursor = connectDB()

        query = """
            SELECT e.stud_id, u.first_name, u.last_name
            FROM enroll e
            JOIN user u ON e.stud_id = u.user_id
            WHERE e.is_approved = FALSE AND e.course_id = %s"""
        
        cursor.execute(query, (course_id,))
        
        waitlist_students = cursor.fetchall()
        
        if not waitlist_students:
            print("No students on the waitlist for this course.")
        else:
            print("Students on the waitlist for course", course_id, ":")
            for stud_id , first_name, last_name in waitlist_students:
                print(f"ID :{stud_id} Name: {first_name} {last_name}")
        return waitlist_students

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

    finally:
        # Ensure the database connection is closed
        cursor.close()
        db_connection.close()

def update_enrollment_status(course_id, student_id):
    try:
        db_connection, cursor = connectDB()

        select_query = """
            SELECT is_approved 
            FROM enroll 
            WHERE course_id = %s AND stud_id = %s """
        
        cursor.execute(select_query, (course_id, student_id))
        current_status = cursor.fetchone()

        # Ensure the student-course combination exists
        if current_status is None:
            print(f"No enrollment record found for student {student_id} in course {course_id}.")
            return False

        # Toggle the current enrollment status
        new_status = not current_status[0]

        # Update the is_approved status for the specified course and student
        update_query = """
            UPDATE enroll 
            SET is_approved = %s 
            WHERE course_id = %s AND stud_id = %s
        """
        cursor.execute(update_query, (new_status, course_id, student_id))
        
        db_connection.commit()
        
        print(f"Enrollment status for student {student_id} in course {course_id} updated to {'approved' if new_status else 'not approved'}.")
        return True

    except Exception as e:
        print(f"An error occurred: {e}")
        return False

    finally:
        # Ensure the database connection is closed
        if cursor:
            cursor.close()
        if db_connection:
            db_connection.close()

def select_students(course_id):
    try:
        db_connection, cursor = connectDB()
        
        select_query = """
            SELECT e.stud_id, u.first_name, u.last_name
            FROM enroll e
            JOIN user u ON e.stud_id = u.user_id
            WHERE e.course_id = %s AND e.is_approved = TRUE
        """
        cursor.execute(select_query, (course_id,))

        students = cursor.fetchall()
        
        # Check if students were found
        if not students:
            print(f"No students enrolled in course {course_id}.")
            return []

        # Print the list of enrolled students
        print(f"Students enrolled in course {course_id}:")
        for student in students:
            print(f"ID: {student[0]}, Name: {student[1]} {student[2]}")
        
        return students

    except Exception as e:
        print(f"An error occurred: {e}")
        return []

    finally:
        cursor.close()
        db_connection.close()

def insert_ta(user_id, first_name, last_name, email, fac_user_id, course_id):
    try:
        db_connection, cursor = connectDB()

        default_password = 'default_pass@123'  
        
        insert_query = """
            INSERT INTO user (user_id, email, first_name, last_name, password, role_no)
            VALUES (%s, %s, %s, %s, %s, 4)"""
        
        cursor.execute(insert_query, (user_id, email, first_name, last_name, default_password))
        db_connection.commit()
        print(f"TA {first_name} {last_name} with ID {user_id} inserted successfully.")

        # Insert into teaching_assistant table
        insert_ta_query = """
            INSERT INTO teaching_assistant (ta_id, course_id, fac_id)
            VALUES (%s, %s, %s)"""
        
        cursor.execute(insert_ta_query, (user_id, course_id, fac_user_id))
        db_connection.commit()
        print(f"TA {user_id} assigned to course {course_id} under faculty {fac_user_id}.")

    except Exception as e:
        print(f"An error occurred while inserting TA: {e}")
        db_connection.rollback()

    finally:
        cursor.close()
        db_connection.close()

def insert_chapter(user_id, course_id, chapter_id, chapter_title):
    try:
        db_connection, cursor = connectDB()
        
        # Query to get the textbook ID based on course_id and user_id (fac_id)
        cursor.execute("""
            SELECT textbook_id
            FROM course
            WHERE course_id = %s AND fac_id = %s
        """, (course_id, user_id))
        
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

def hide_chapter_util(user_id, course_id, chapter_id):
    try:
        db_connection, cursor = connectDB()
        textbook_id = get_textbook_id(course_id, user_id)
        # Check the role of the user
        cursor.execute("""
            SELECT u.role_no
            FROM user u
            JOIN chapter c ON c.updated_by = u.user_id
            WHERE c.chapter_id = %s AND c.textbook_id =%s AND u.user_id = %s
        """, (chapter_id,textbook_id, user_id))
        
        result = cursor.fetchone()
        if result is not None:
            role_no = result[0]
            # Proceed to update if role_no is not 1
            if role_no != 100:
                cursor.execute("""
                    UPDATE chapter
                    SET is_hidden = %s, updated_by = %s
                    WHERE chapter_id = %s AND textbook_id = %s
                """, (True, user_id, chapter_id, textbook_id))
                db_connection.commit()

                # Check if any rows were affected
                if cursor.rowcount > 0:
                    print("Chapter hidden successfully.")
                    return True
                else:
                    print("No chapter found with the given chapter_id or course_id.")
                    return False
            else:
                print("User role does not permit hiding the chapter.")
                return False
        else:
            print("Chapter not found for the given chapter_id.")
            return False

    except Exception as e:
        print("Error hiding chapter:", e)
        return False

def del_chapter(user_id, course_id, chapter_id):
    try:
        # Establish the database connection
        db_connection, cursor = connectDB()
        textbook_id = get_textbook_id(course_id, user_id)
        # Check the role of the user
        cursor.execute("""
            SELECT u.role_no
            FROM user u
            JOIN chapter c ON c.updated_by = u.user_id
            WHERE c.chapter_id = %s AND c.textbook_id =%s AND u.user_id = %s
        """, (chapter_id,textbook_id, user_id))
        
        result = cursor.fetchone()
        if result is not None:
            role_no = result[0]
            # Proceed to delete if role_no is not 1
            if role_no != 1:
                cursor.execute("""
                    DELETE FROM chapter
                    WHERE chapter_id = %s AND textbook_id = %s
                """, (chapter_id,textbook_id ))

                # Commit the changes
                db_connection.commit()
                print("Chapter deleted successfully.")
                return True
            else:
                print("User role does not permit deletion of the chapter.")
                return False
        else:
            print("Chapter not found for the given chapter_id.")
            return False

    except Exception as e:
        print("Error deleting chapter:", e)
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
            WHERE course_id = %s AND fac_id = %s
        """, (course_id, user_id))

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

def hide_section_util(user_id, course_id, chapter_id, section_id):
    try:
        db_connection, cursor = connectDB()
        textbook_id = get_textbook_id(course_id, user_id)
        cursor.execute("""
            SELECT u.role_no
            FROM user u
            JOIN section s ON u.user_id = s.updated_by
            WHERE s.textbook_id = %s AND s.chapter_id = %s AND s.section_id = %s AND u.user_id = %s
        """, (textbook_id, chapter_id, section_id, user_id))

        result = cursor.fetchone()
        if result and result[0] != 100: 
            # Update the section to hide it
            cursor.execute("""
                UPDATE section
                SET is_hidden = TRUE, updated_by = %s
                WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s
            """, (user_id, textbook_id, chapter_id, section_id))
            
            db_connection.commit()
            print("Section successfully hidden.")
            return True
        else:
            print("User does not have permission to hide this section.")
            return False

    except Exception as e:
        db_connection.rollback()
        print("Error hiding section:", e)
        return False
    finally:
        cursor.close()
        db_connection.close()

def del_section(user_id, course_id, chapter_id, section_id):
    try:
        db_connection, cursor = connectDB()
        textbook_id = get_textbook_id(course_id, user_id)
        cursor.execute("""
            SELECT u.role_no
            FROM user u
            JOIN section s ON s.updated_by = u.user_id
            WHERE s.section_id = %s AND s.chapter_id = %s AND s.textbook_id = %s AND u.user_id = %s
        """, (section_id, chapter_id, textbook_id, user_id))
        
        result = cursor.fetchone()
        if result is not None:
            role_no = result[0]
            # Proceed to delete if role_no is not 1
            if role_no != 1:
                cursor.execute("""
                    DELETE FROM section
                    WHERE section_id = %s AND chapter_id = %s AND textbook_id = %s
                """, (section_id, chapter_id, textbook_id))

                # Commit the changes
                db_connection.commit()
                print("Section deleted succesfully")
                return True
                
            else:
                print("User role does not permit deletion of the section.")
                return False
        else:
            print("Section not found for the given section_id and chapter_id.")
            return False

    except Exception as e:
        print("Error deleting section:", e)
        return False

    finally:
        cursor.close()
        db_connection.close()

def insert_content_block(user_id, course_id, chapter_id, section_id, block_id, is_type):
    try:
        db_connection, cursor = connectDB()
        textbook_id = get_textbook_id(course_id, user_id)
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
    
def insert_text(textbook_id, chapter_id, section_id, block_id, text_id, text_content):
    try:
        db_connection, cursor = connectDB()
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

def insert_image(textbook_id, chapter_id, section_id, block_id, image_id, image_content, alt_text):
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
        print("New activity created successfully.")
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

def hide_content_block_util(user_id, course_id, chapter_id, section_id, block_id):
    try:
        db_connection, cursor = connectDB()
        textbook_id = get_textbook_id(course_id, user_id)

        # Check if the user has permission to hide the content block
        cursor.execute("""
            SELECT u.role_no
            FROM user u
            JOIN content_block cb ON u.user_id = cb.updated_by
            WHERE cb.textbook_id = %s AND cb.chapter_id = %s AND cb.section_id = %s AND cb.block_id = %s AND u.user_id = %s
        """, (textbook_id, chapter_id, section_id, block_id, user_id))

        result = cursor.fetchone()
        # If the role_no is not admin (assuming 1 is the admin role)
        if result and result[0] != 100:
            cursor.execute("""
                UPDATE content_block
                SET is_hidden = TRUE, updated_by = %s
                WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s AND block_id = %s
            """, (user_id, textbook_id, chapter_id, section_id, block_id))
            
            db_connection.commit()
            print("Content block successfully hidden.")
            return True
        else:
            print("User does not have permission to hide this content block.")
            return False

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
        textbook_id = get_textbook_id(course_id, user_id)
        
        cursor.execute("""
            SELECT u.role_no
            FROM user u
            JOIN content_block cb ON cb.updated_by = u.user_id
            WHERE cb.block_id = %s AND cb.section_id = %s AND cb.chapter_id = %s AND cb.textbook_id = %s AND u.user_id = %s
        """, (block_id, section_id, chapter_id, textbook_id, user_id))
        
        result = cursor.fetchone()
        
        if result is not None:
            role_no = result[0]
            # Proceed to delete if role_no is not 1 (admin role)
            if role_no != 1:
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

def hide_activity_util(user_id, course_id, chapter_id, section_id, block_id, activity_id):
    try:
        db_connection, cursor = connectDB()
        textbook_id = get_textbook_id(course_id, user_id)
        cursor.execute("""
            SELECT u.role_no
            FROM user u
            JOIN activity a ON u.user_id = a.updated_by
            WHERE a.textbook_id = %s AND a.chapter_id = %s AND a.section_id = %s AND a.block_id = %s AND a.activity_id = %s AND u.user_id = %s
        """, (textbook_id, chapter_id, section_id, block_id, activity_id, user_id))

        result = cursor.fetchone()
        # If the role_no is not admin (assuming 1 is the admin role)
        if result and result[0] != 100:
            # Update the activity to hide it
            cursor.execute("""
                UPDATE activity
                SET is_hidden = TRUE, updated_by = %s
                WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s AND block_id = %s AND activity_id = %s
            """, (user_id, textbook_id, chapter_id, section_id, block_id, activity_id))
            
            db_connection.commit()
            print("Activity successfully hidden.")
            return True
        else:
            print("User does not have permission to hide this activity.")
            return False

    except Exception as e:
        db_connection.rollback()
        print("Error hiding activity:", e)
        return False
    finally:
        cursor.close()
        db_connection.close()

def del_activity(user_id, course_id, chapter_id, section_id, block_id, activity_id):
    try:
        db_connection, cursor = connectDB()
        textbook_id = get_textbook_id(course_id, user_id)

        cursor.execute("""
            SELECT u.role_no
            FROM user u
            JOIN activity a ON a.updated_by = u.user_id
            WHERE a.activity_id = %s AND a.block_id = %s AND a.section_id = %s AND a.chapter_id = %s 
                  AND a.textbook_id = %s AND u.user_id = %s
        """, (activity_id, block_id, section_id, chapter_id, textbook_id, user_id))
        
        result = cursor.fetchone()
        
        if result is not None:
            role_no = result[0]
            # Proceed to delete if role_no is not 1 (admin role)
            if role_no != 1:
                cursor.execute("""
                    DELETE FROM activity
                    WHERE activity_id = %s AND block_id = %s AND section_id = %s AND chapter_id = %s AND textbook_id = %s
                """, (activity_id, block_id, section_id, chapter_id, textbook_id))

                db_connection.commit()
                print("Activity deleted successfully.")
                return True
            else:
                print("User role does not permit deletion of the activity.")
                return False
        else:
            print("Activity not found for the given block_id, section_id, and chapter_id.")
            return False

    except Exception as e:
        print("Error deleting activity:", e)
        return False

    finally:
        cursor.close()
        db_connection.close()