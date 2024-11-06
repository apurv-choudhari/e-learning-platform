from db_utils import connectDB
from utils.validate_credentials import login_flow
import mysql.connector
import datetime
import random
from app import main_menu

def generate_unique_user_id(first_name, last_name, cursor):
    while True:
        user_id = f"{first_name[:2]}{last_name[:2]}{random.randint(1000, 9999)}"
        cursor.execute("SELECT COUNT(*) FROM user WHERE user_id = %s", (user_id,))
        if cursor.fetchone()[0] == 0:
            return user_id

def enroll_in_course():
    reservationConnection, cursor = connectDB()
    if not cursor:
        return
    
    try:
        print("Enter the following details:")
        first_name = input("First Name: ").strip()
        last_name = input("Last Name: ").strip()
        email = input("Email: ").strip()
        course_token = input("Course Token: ").strip()
        
        cursor.execute("SELECT course_id FROM active_course WHERE token = %s", (course_token,))
        course_result = cursor.fetchone()
        
        if not course_result:
            print("Invalid course token.")
            return
        
        course_id = course_result[0]
        
        cursor.execute("SELECT user_id FROM user WHERE email = %s", (email,))
        user_result = cursor.fetchone()
        
        if user_result:
            user_id = user_result[0]
            
            cursor.execute("SELECT is_approved FROM enroll WHERE stud_id = %s AND course_id = %s", (user_id, course_id))
            enroll_result = cursor.fetchone()
            
            if enroll_result:
                if enroll_result[0]:
                    print("You are already enrolled in the course.")
                else:
                    print("You already have a pending enrollment request for this course.")
            else:
                cursor.execute("INSERT INTO enroll (is_approved, stud_id, course_id) VALUES (FALSE, %s, %s)", (user_id, course_id))
                reservationConnection.commit()
                print("Enrollment request created.")
        else:
            user_id = generate_unique_user_id(first_name, last_name, cursor)
            default_password = "default_password"
            
            cursor.execute("""
                INSERT INTO user (user_id, email, first_name, last_name, password, role_no) 
                VALUES (%s, %s, %s, %s, %s, 3)
            """, (user_id, email, first_name, last_name, default_password))
            
            cursor.execute("INSERT INTO student (stud_id) VALUES (%s)", (user_id,))
            
            cursor.execute("INSERT INTO enroll (is_approved, stud_id, course_id) VALUES (FALSE, %s, %s)", (user_id, course_id))
            reservationConnection.commit()
            
            print("New user and enrollment request created successfully.")
            print(f"\nYour account has been created successfully!")
            print(f"User ID: {user_id}")
            print(f"Password: {default_password} (please change after logging in)")

        while True:
            print("\nMenu:")
            print("1. Enroll")
            print("2. Go Back")
            choice = input("Choose option (1-2): ")
            
            if choice == '1':
                enroll_in_course()
                break
            elif choice == '2':
                print("Going back to the main menu.")
                break
            else:
                print("Invalid choice. Please enter a valid option.")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        cursor.close()
        reservationConnection.close()

def view_section(user_id):
    reservationConnection, cursor = connectDB()
    if not cursor:
        return

    try:
        print("\n--- View Section ---")

        cursor.execute(""" 
            SELECT course_id FROM enroll WHERE stud_id = %s AND is_approved = TRUE
        """, (user_id,))
        enrolled_courses = cursor.fetchall()

        if not enrolled_courses:
            print("You are not enrolled in any courses.")
            return

        available_sections = {}

        for course in enrolled_courses:
            course_id = course[0]

            cursor.execute("""
                SELECT textbook.title AS textbook_title, textbook.textbook_id 
                FROM textbook
                JOIN course ON course.textbook_id = textbook.textbook_id
                WHERE course.course_id = %s
            """, (course_id,))
            textbook = cursor.fetchone()

            if textbook:
                cursor.execute("""
                    SELECT chapter_id, title AS chapter_title FROM chapter WHERE textbook_id = %s AND is_hidden = FALSE
                """, (textbook[1],))
                chapters = cursor.fetchall()

                for chapter in chapters:
                    chapter_id = chapter[0]
                    cursor.execute("""
                        SELECT section_id, title AS section_title FROM section 
                        WHERE textbook_id = %s AND chapter_id = %s AND is_hidden = FALSE
                    """, (textbook[1], chapter_id))
                    sections = cursor.fetchall()

                    for section in sections:
                        section_id = section[0]
                        available_sections[(course_id, chapter_id, section_id)] = section[1]

        if not available_sections:
            print("No available sections to view.")
            return

        print("\nAvailable Sections:")
        for (course_id, chapter_id, section_id), section_title in available_sections.items():
            print(f"Course ID: {course_id}, Chapter ID: {chapter_id}, Section ID: {section_id} - {section_title}")

        course_id_input = input("\nEnter Course ID: ")
        chapter_id_input = input("Enter Chapter ID: ")
        section_id_input = input("Enter Section ID: ")

        cursor.execute("""
            SELECT section_id FROM section 
            WHERE textbook_id = (
            SELECT textbook_id FROM course WHERE course_id = %s
            ) AND chapter_id = %s AND section_id = %s AND is_hidden = FALSE
        """, (course_id_input, chapter_id_input, section_id_input))

        section_available = cursor.fetchone()

        if not section_available:
            print("Invalid section or invalid access request. Please try again.")
            return

        print("\nMenu:")
        print("1. View Block")
        print("2. Go Back")
        choice = input("Choose an option (1-2): ")

        if choice == '1':
            view_block(user_id, course_id_input, chapter_id_input, section_id_input)
        elif choice == '2':
            print("Going back to the landing page.")
            return
        else:
            print("Invalid choice. Please enter a valid option.")
            return

    except mysql.connector.Error as err:
        print('Error:', err)
    finally:
        cursor.close()
        reservationConnection.close()

def submit_answers(user_id, textbook_id, chapter_id, section_id, block_id, answers):
    reservationConnection, cursor = connectDB()
    if not cursor:
        return

    try:
        cursor = reservationConnection.cursor(buffered=True)
        
        cursor.execute("""SELECT course_id FROM course WHERE textbook_id = %s""", (textbook_id,))
        course_data = cursor.fetchone()

        if not course_data:
            print("No course found for the given textbook_id.")
            return

        course_id = course_data[0]
        print(f"Using course_id: {course_id}")

        cursor.execute("""SELECT activity_id FROM activity WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s AND block_id = %s""",
                       (textbook_id, chapter_id, section_id, block_id))
        activity_data = cursor.fetchone()

        if not activity_data:
            print(f"No activity_id found for the block_id {block_id}.")
            return

        activity_id = activity_data[0]
        print(f"Using activity_id: {activity_id}")

        for question_id, user_answer in answers:
            cursor.execute("""SELECT * FROM score WHERE question_id = %s AND block_id = %s AND stud_id = %s""",
                           (question_id, block_id, user_id))
            existing_score = cursor.fetchone()

            if existing_score:
                print(f"This question was already attempted before. Scores will not be updated.")
                continue

            cursor.execute("""SELECT correct_answer FROM question WHERE question_id = %s""", (question_id,))
            correct_answer_data = cursor.fetchone()

            if not correct_answer_data:
                print(f"No correct answer found for question {question_id}")
                continue

            correct_answer = correct_answer_data[0]
            score = 3 if user_answer == correct_answer else 1

            timestamp = datetime.datetime.now()
            cursor.execute("""INSERT INTO score (course_id, textbook_id, chapter_id, section_id, block_id,
                                                  activity_id, question_id, score, timestamp, stud_id)
                              VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                           (course_id, textbook_id, chapter_id, section_id, block_id, activity_id, question_id,
                            score, timestamp, user_id))

        reservationConnection.commit()
        print("Scores submitted successfully.")

    except mysql.connector.Error as err:
        print('Error:', err)
    finally:
        cursor.close()
        reservationConnection.close()

def view_block(user_id, course_id, chapter_id, section_id):
    reservationConnection, cursor = connectDB()
    if not cursor:
        return

    try:
        print("\n--- View Block ---")

        cursor.execute("""SELECT textbook_id FROM course WHERE course_id = %s""", (course_id,))
        course_data = cursor.fetchone()

        if not course_data:
            print("Invalid course_id. Course not found.")
            return

        textbook_id = course_data[0]
        print(f"Using textbook_id: {textbook_id}")

        cursor.fetchall()

        cursor.execute("""SELECT block_id, is_type FROM content_block
                          WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s""",
                       (textbook_id, chapter_id, section_id))
        block = cursor.fetchone()

        if not block:
            print("No block found for the given textbook, chapter, and section.")
            return

        block_id, block_type = block

        cursor.fetchall()

        print(f"\nBlock Content for Block ID {block_id}:")

        if block_type == 'text':
            cursor.execute("""SELECT text_content FROM text
                              WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s AND block_id = %s""",
                           (textbook_id, chapter_id, section_id, block_id))
            text_content = cursor.fetchone()
            if text_content:
                print(text_content[0])
            else:
                print("No text content found.")

            print("\nMenu:")
            print("1. Next")
            print("2. Go back")
            choice = input("Choose an option (1-2): ")

            if choice == '1':
                student_landing_page(user_id)
            elif choice == '2':
                view_section(user_id)
            else:
                print("Invalid choice. Please enter a valid option.")
                return

        elif block_type == 'picture':
            cursor.execute("""SELECT image_content, alt_text FROM image
                              WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s AND block_id = %s""",
                           (textbook_id, chapter_id, section_id, block_id))
            image_content = cursor.fetchone()
            if image_content:
                print(f"Image: {image_content[0]}")
                print(f"Alt text: {image_content[1]}")
            else:
                print("No image content found.")

            print("\nMenu:")
            print("1. Next")
            print("2. Go back")
            choice = input("Choose an option (1-2): ")

            if choice == '1':
                student_landing_page(user_id)
            elif choice == '2':
                view_section(user_id)
            else:
                print("Invalid choice. Please enter a valid option.")
                return

        elif block_type == 'activity':
            cursor.execute("""SELECT question_id, question_text, option1, option2, option3, option4,
                              option1_explanation, option2_explanation, option3_explanation, option4_explanation
                              FROM question
                              WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s AND block_id = %s""",
                           (textbook_id, chapter_id, section_id, block_id))
            questions = cursor.fetchall()

            if not questions:
                print("No questions found for this activity.")
                return

            print("Activity Questions:")
            answers = []
            for question in questions:
                question_id, question_text, option1, option2, option3, option4, \
                option1_explanation, option2_explanation, option3_explanation, option4_explanation = question

                print(f"\n{question_text}")
                print(f"1. {option1}")
                print(f"2. {option2}")
                print(f"3. {option3}")
                print(f"4. {option4}")
                user_answer = input("Choose the correct option (1-4): ")

                if user_answer == '1':
                    print(f"Explanation for option 1: {option1_explanation}")
                elif user_answer == '2':
                    print(f"Explanation for option 2: {option2_explanation}")
                elif user_answer == '3':
                    print(f"Explanation for option 3: {option3_explanation}")
                elif user_answer == '4':
                    print(f"Explanation for option 4: {option4_explanation}")
                else:
                    print("Invalid option, no explanation available.")

                answers.append((question_id, user_answer))

            print("\nMenu:")
            print("1. Next/Submit")
            print("2. Back")
            choice = input("Choose an option (1-2): ")

            if choice == '1':
                submit_answers(user_id, textbook_id, chapter_id, section_id, block_id, answers)
                print("Answers submitted successfully.")
                student_landing_page(user_id)
            elif choice == '2':
                print("Going back to the section.")
                view_section(user_id)
            else:
                print("Invalid choice. Please enter a valid option.")
                return

        else:
            print("Unknown block type.")

    except mysql.connector.Error as err:
        print('Error:', err)
    finally:
        cursor.close()
        reservationConnection.close()

def view_participation_points(student_id):
    reservationConnection, cursor = connectDB()
    if not cursor:
        return

    try:
        query_student_score = """
            SELECT 
                sc.course_id, 
                sc.textbook_id, 
                sc.chapter_id, 
                sc.section_id, 
                sc.block_id, 
                sc.activity_id, 
                SUM(CASE WHEN sc.score IS NOT NULL THEN sc.score ELSE 0 END) AS student_score  -- Sum the student's scores
            FROM score sc
            WHERE sc.stud_id = %s
            GROUP BY sc.course_id, sc.textbook_id, sc.chapter_id, sc.section_id, sc.block_id, sc.activity_id
        """

        cursor.execute(query_student_score, (student_id,))
        student_scores = cursor.fetchall()

        if not student_scores:
            print(f"No participation points found for student {student_id}.")
            return

        print(f"Participation Points for Student {student_id}:")
        
        for row in student_scores:
            course_id, textbook_id, chapter_id, section_id, block_id, activity_id, student_score = row

            query_total_questions = """
                SELECT COUNT(question_id) AS total_questions
                FROM question
                WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s AND block_id = %s AND activity_id = %s
            """
            cursor.execute(query_total_questions, (textbook_id, chapter_id, section_id, block_id, activity_id))
            total_questions = cursor.fetchone()[0]

            total_possible_score = total_questions * 3

            print(f"\nCourse: {course_id}, Textbook: {textbook_id}, Chapter: {chapter_id}, Section: {section_id}")
            print(f"Activity: {activity_id}")
            print(f"Student Score: {student_score}")
            print(f"Total Possible Score: {total_possible_score}")

        while True:
            print("\nMenu:")
            print("1. Go back")
            choice = input("Choose option (1): ")
            
            if choice == '1':
                print("Going back to the landing page.")
                break  
            else:
                print("Invalid choice. Please enter a valid option.")
    
    except Exception as e:
        print("An error occurred:", e)
    finally:
        cursor.close()
        reservationConnection.close()

def student_landing_page(user_id):
    reservationConnection, cursor = connectDB()
    if not cursor:
        return

    try:
        ebook_count = 1  # Initialize a counter for E-books
        while True:
            print("\n--- Student Landing Page ---")

            cursor.execute("""SELECT course_id FROM enroll WHERE stud_id = %s AND is_approved = TRUE""", (user_id,))
            enrolled_courses = cursor.fetchall()

            if not enrolled_courses:
                print("You are not enrolled in any courses.")
                return

            for course in enrolled_courses:
                course_id = course[0]

                cursor.execute("""SELECT textbook.title AS textbook_title 
                    FROM textbook
                    JOIN course ON course.textbook_id = textbook.textbook_id
                    WHERE course.course_id = %s
                """, (course_id,))
                textbook = cursor.fetchone()

                if textbook:
                    textbook_title = textbook[0]
                    print(f"\nE-book {ebook_count}: {textbook_title} (Course ID: {course_id})")
                    ebook_count += 1  # Increment for each new E-book

                    cursor.execute("""SELECT chapter_id, title AS chapter_title 
                        FROM chapter 
                        WHERE textbook_id = (
                            SELECT textbook_id FROM course WHERE course_id = %s
                        ) AND is_hidden = FALSE
                    """, (course_id,))
                    chapters = cursor.fetchall()

                    chapter_count = 1  # Counter for chapters
                    for chapter in chapters:
                        chapter_id, chapter_title = chapter
                        print(f"  Chapter {chapter_count}: {chapter_title}")
                        chapter_count += 1  # Increment for each new chapter

                        cursor.execute("""SELECT section_id, title AS section_title 
                            FROM section 
                            WHERE chapter_id = %s AND textbook_id = (
                                SELECT textbook_id FROM course WHERE course_id = %s
                            ) AND is_hidden = FALSE
                        """, (chapter_id, course_id))
                        sections = cursor.fetchall()

                        section_count = 1  # Counter for sections
                        for section in sections:
                            section_id, section_title = section
                            print(f"    Section {section_count}: {section_title}")
                            section_count += 1  # Increment for each new section

                            cursor.execute("""SELECT block_id, is_type 
                                FROM content_block 
                                WHERE chapter_id = %s AND section_id = %s AND textbook_id = (
                                    SELECT textbook_id FROM course WHERE course_id = %s
                                ) AND is_hidden = FALSE
                            """, (chapter_id, section_id, course_id))
                            blocks = cursor.fetchall()

                            block_count = 1  # Counter for blocks
                            for block in blocks:
                                block_id, block_type = block
                                print(f"      Block {block_count}: {block_type}")
                                block_count += 1  # Increment for each new block

            print("\nMenu:")
            print("1. View a Section")
            print("2. View Participation Activity Points")
            print("3. Logout")
            choice = input("Choose option (1-3): ")

            if choice == '1':
                view_section(user_id)
            elif choice == '2':
                results = view_participation_points(user_id)
                if results:
                    print("\nParticipation Activity Points:")
                    for activity in results:
                        print(f"Activity ID: {activity['activity_id']}, Score: {activity['score']}/{activity['total_points']} points")
                else:
                    print("No participation activities found.")
            elif choice == '3':
                print("Logging out.")
                main_menu()
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    except mysql.connector.Error as err:
        print('Error:', err)
    finally:
        cursor.close()
        reservationConnection.close()