from db_utils import connectDB
from utils.validate_credentials import login_flow
import mysql.connector
import datetime
from app import main_menu

def student_flow(user_id):
    while True:
        print("\nWelcome to Student Main Menu:")
        print("1. Enroll in a Course")
        print("2. Sign-In")
        print("3. Go Back")
        choice = input("Choose an option (1-3): ")

        if choice == '1':
            enroll_in_course(user_id)
        elif choice == '2':
            sign_in_flow(user_id)  # Pass user_id to sign_in_flow
        elif choice == '3':
            print("Returning to the main menu.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def enroll_in_course(user_id):
    print("\n--- Enroll in a Course ---")
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    email = input("Enter Email: ")
    course_token = input("Enter Course Token: ")

    print("\n1. Enroll")
    print("2. Go Back")
    choice = input("Choose an option (1-2): ")

    if choice == '1':
        # Code to create account and add student to waiting list
        enroll_student(user_id, course_token)  # Now calls enroll_student to enroll the user in a course
    elif choice == '2':
        print("Returning to Student Main Menu.")
    else:
        print("Invalid choice. Returning to Student Main Menu.")

def sign_in_flow(user_id):
    user_id, login_success = login_flow(3)

    if login_success:
        student_landing_page(user_id)
    else:
        print("Invalid credentials, returning to student main menu")

def student_landing_page(user_id):
    # Connect to the database
    reservationConnection, cursor = connectDB()
    if not cursor:
        return

    try:
        while True:
            print("\n--- Student Landing Page ---")

            # Step 1: Get all courses the student is enrolled in
            cursor.execute("""
                SELECT course_id FROM enroll WHERE stud_id = %s AND is_approved = TRUE
            """, (user_id,))
            enrolled_courses = cursor.fetchall()

            if not enrolled_courses:
                print("You are not enrolled in any courses.")
                return

            for course in enrolled_courses:
                course_id = course[0]

                # Get the textbook for the course
                cursor.execute("""
                    SELECT textbook.title AS textbook_title 
                    FROM textbook
                    JOIN course ON course.textbook_id = textbook.textbook_id
                    WHERE course.course_id = %s
                """, (course_id,))
                textbook = cursor.fetchone()

                if textbook:
                    textbook_title = textbook[0]
                    print(f"\nE-book: {textbook_title} (Course ID: {course_id})")  # Display the textbook title with course ID

                    # Get chapters for the textbook
                    cursor.execute("""
                        SELECT chapter_id, title AS chapter_title FROM chapter WHERE textbook_id = (
                            SELECT textbook_id FROM course WHERE course_id = %s
                        )
                    """, (course_id,))
                    chapters = cursor.fetchall()

                    for chapter in chapters:
                        chapter_id, chapter_title = chapter
                        print(f"  Chapter: {chapter_title}")

                        # Get sections for the chapter
                        cursor.execute("""
                            SELECT section_id, title AS section_title FROM section 
                            WHERE chapter_id = %s AND textbook_id = (
                                SELECT textbook_id FROM course WHERE course_id = %s
                            )
                        """, (chapter_id, course_id))
                        sections = cursor.fetchall()

                        for section in sections:
                            section_id, section_title = section
                            print(f"    Section: {section_title}")

                            # Get blocks for the section
                            cursor.execute("""
                                SELECT block_id, is_type FROM content_block 
                                WHERE chapter_id = %s AND section_id = %s AND textbook_id = (
                                    SELECT textbook_id FROM course WHERE course_id = %s
                                )
                            """, (chapter_id, section_id, course_id))
                            blocks = cursor.fetchall()

                            for block in blocks:
                                block_id, block_type = block
                                print(f"      Block: {block_type}")

            # Step 3: Show the menu after displaying the contents
            print("\nMenu:")
            print("1. View a Section")
            print("2. View Participation Activity Points")
            print("3. Logout")
            choice = input("Choose option (1-3): ")

            if choice == '1':
                view_section(user_id)  # Pass user_id to view_section
            elif choice == '2':
                view_participation_points(user_id)
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




def view_section(user_id):
    # Connect to the database
    reservationConnection, cursor = connectDB()
    if not cursor:
        return

    try:
        print("\n--- View Section ---")

        # Step 1: Get all courses the student is enrolled in
        cursor.execute(""" 
            SELECT course_id FROM enroll WHERE stud_id = %s AND is_approved = TRUE
        """, (user_id,))
        enrolled_courses = cursor.fetchall()

        if not enrolled_courses:
            print("You are not enrolled in any courses.")
            return

        # Step 2: Get course_id, chapter_id, and section_id that are available to the student
        available_sections = {}

        for course in enrolled_courses:
            course_id = course[0]

            # Get the textbook for the course
            cursor.execute("""
                SELECT textbook.title AS textbook_title, textbook.textbook_id 
                FROM textbook
                JOIN course ON course.textbook_id = textbook.textbook_id
                WHERE course.course_id = %s
            """, (course_id,))
            textbook = cursor.fetchone()

            if textbook:
                # Get chapters for the textbook
                cursor.execute("""
                    SELECT chapter_id, title AS chapter_title FROM chapter WHERE textbook_id = %s
                """, (textbook[1],))
                chapters = cursor.fetchall()

                for chapter in chapters:
                    chapter_id = chapter[0]
                    # Get sections for the chapter
                    cursor.execute("""
                        SELECT section_id, title AS section_title FROM section 
                        WHERE textbook_id = %s AND chapter_id = %s
                    """, (textbook[1], chapter_id))
                    sections = cursor.fetchall()

                    for section in sections:
                        section_id = section[0]
                        available_sections[(course_id, chapter_id, section_id)] = section[1]

        if not available_sections:
            print("No available sections to view.")
            return

        # Step 3: Ask the student to input course_id, chapter_id, and section_id
        print("\nAvailable Sections:")
        for (course_id, chapter_id, section_id), section_title in available_sections.items():
            print(f"Course ID: {course_id}, Chapter ID: {chapter_id}, Section ID: {section_id} - {section_title}")

        # Prompt the user for input
        course_id_input = input("\nEnter Course ID: ")
        chapter_id_input = input("Enter Chapter ID: ")
        section_id_input = input("Enter Section ID: ")

        # Validate the input
        if (course_id_input, chapter_id_input, section_id_input) not in available_sections:
            print("Invalid combination of Course ID, Chapter ID, and Section ID. Please try again.")
            return

        # Step 4: Present the options
        print("\nMenu:")
        print("1. View Block")
        print("2. Go Back")
        choice = input("Choose an option (1-2): ")

        if choice == '1':
            view_block(user_id, course_id_input, chapter_id_input, section_id_input)  # Call the view_block function
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




# def enroll_student(user_id, course_token):
#     # Connect to the database
#     reservationConnection, cursor = connectDB()
#     if not cursor:
#         return

#     try:
#         # Check if the course token exists in active courses
#         cursor.execute("""
#             SELECT capacity FROM active_course WHERE token = %s
#         """, (course_token,))
#         course = cursor.fetchone()

#         if not course:
#             print("Invalid course token. Returning to menu.")
#             return

#         capacity = course[0]

#         # Insert the student into the enroll table (assuming the student is not already enrolled)
#         cursor.execute("""
#             INSERT INTO enroll (stud_id, course_id, is_approved) 
#             VALUES (%s, %s, FALSE)
#         """, (user_id, course_token))
#         reservationConnection.commit()
#         print("Enrollment request recorded. Account created if this is the first request.")

#     except mysql.connector.Error as err:
#         print('Error:', err)
#     finally:
#         cursor.close()
#         reservationConnection.close()








# def view_block(user_id, course_id, chapter_id, section_id):
#     # Connect to the database
#     reservationConnection, cursor = connectDB()
#     if not cursor:
#         return

#     try:
#         print("\n--- View Block ---")

#         # Step 1: Fetch the textbook_id from the course table using the course_id
#         cursor.execute("""SELECT textbook_id FROM course WHERE course_id = %s""", (course_id,))
#         course_data = cursor.fetchone()

#         if not course_data:
#             print("Invalid course_id. Course not found.")
#             return

#         textbook_id = course_data[0]
#         print(f"Using textbook_id: {textbook_id}")

#         # Ensure previous results are discarded
#         cursor.fetchall()  # Discards any remaining results from the previous query

#         # Step 2: Get the block details based on the textbook_id, chapter_id, and section_id
#         cursor.execute("""SELECT block_id, is_type FROM content_block
#                           WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s""",
#                        (textbook_id, chapter_id, section_id))
#         block = cursor.fetchone()

#         if not block:
#             print("No block found for the given textbook, chapter, and section.")
#             return

#         block_id, block_type = block

#         # Ensure previous results are discarded
#         cursor.fetchall()  # Discards any remaining results from the previous query

#         # Step 3: Display content based on block type
#         print(f"\nBlock Content for Block ID {block_id}:")

#         if block_type == 'text':
#             # Fetch content from the text table for text blocks
#             cursor.execute("""SELECT text_content FROM text
#                               WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s AND block_id = %s""",
#                            (textbook_id, chapter_id, section_id, block_id))
#             text_content = cursor.fetchone()
#             if text_content:
#                 print(text_content[0])  # Show the text content
#             else:
#                 print("No text content found.")

#             # Ensure previous results are discarded
#             cursor.fetchall()

#         elif block_type == 'picture':
#             # Fetch content from the image table for image blocks
#             cursor.execute("""SELECT image_content, alt_text FROM image
#                               WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s AND block_id = %s""",
#                            (textbook_id, chapter_id, section_id, block_id))
#             image_content = cursor.fetchone()
#             if image_content:
#                 print(f"Image: {image_content[0]}")  # Show image content (filename)
#                 print(f"Alt text: {image_content[1]}")  # Show alt text for the image
#             else:
#                 print("No image content found.")

#             # Ensure previous results are discarded
#             cursor.fetchall()

#         elif block_type == 'activity':
#             # Fetch activity questions
#             cursor.execute("""SELECT question_id, question_text, option1, option2, option3, option4,
#                               option1_explanation, option2_explanation, option3_explanation, option4_explanation
#                               FROM question
#                               WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s AND block_id = %s""",
#                            (textbook_id, chapter_id, section_id, block_id))
#             questions = cursor.fetchall()

#             if not questions:
#                 print("No questions found for this activity.")
#                 return

#             print("Activity Questions:")
#             answers = []
#             for question in questions:
#                 question_id, question_text, option1, option2, option3, option4, \
#                 option1_explanation, option2_explanation, option3_explanation, option4_explanation = question

#                 print(f"\n{question_text}")  # Display question text
#                 print(f"1. {option1}")
#                 print(f"2. {option2}")
#                 print(f"3. {option3}")
#                 print(f"4. {option4}")
#                 user_answer = input("Choose the correct option (1-4): ")

#                 # Show the explanation for the selected option immediately
#                 if user_answer == '1':
#                     print(f"Explanation for option 1: {option1_explanation}")
#                 elif user_answer == '2':
#                     print(f"Explanation for option 2: {option2_explanation}")
#                 elif user_answer == '3':
#                     print(f"Explanation for option 3: {option3_explanation}")
#                 elif user_answer == '4':
#                     print(f"Explanation for option 4: {option4_explanation}")
#                 else:
#                     print("Invalid option, no explanation available.")

#                 # Collect the answers
#                 answers.append((question_id, user_answer))

#             # Show the options for next/submit
#             print("\nMenu:")
#             print("1. Submit Answers")
#             print("2. Back")
#             choice = input("Choose an option (1-2): ")

#             if choice == '1':
#                 submit_answers(user_id, textbook_id, chapter_id, section_id, block_id, answers)
#                 print("Answers submitted successfully.")
#                 student_landing_page(user_id)  # Go back to the landing page
#             elif choice == '2':
#                 print("Going back to the section.")
#                 view_section(user_id)  # Go back to the view_section page
#             else:
#                 print("Invalid choice. Please enter a valid option.")
#                 return

#         else:
#             print("Unknown block type.")

#     except mysql.connector.Error as err:
#         print('Error:', err)
#     finally:
#         cursor.close()
#         reservationConnection.close()

def submit_answers(user_id, textbook_id, chapter_id, section_id, block_id, answers):
    # Connect to the database
    reservationConnection, cursor = connectDB()
    if not cursor:
        return

    try:
        # Create a buffered cursor
        cursor = reservationConnection.cursor(buffered=True)  # <-- Add this line here
        
        # Step 1: Fetch course_id from textbook_id
        cursor.execute("""SELECT course_id FROM course WHERE textbook_id = %s""", (textbook_id,))
        course_data = cursor.fetchone()

        if not course_data:
            print("No course found for the given textbook_id.")
            return

        course_id = course_data[0]
        print(f"Using course_id: {course_id}")

        # Step 2: Fetch activity_id based on block_id from the activity table
        cursor.execute("""SELECT activity_id FROM activity WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s AND block_id = %s""",
                       (textbook_id, chapter_id, section_id, block_id))
        activity_data = cursor.fetchone()

        if not activity_data:
            print(f"No activity_id found for the block_id {block_id}.")
            return

        activity_id = activity_data[0]
        print(f"Using activity_id: {activity_id}")

        # Step 3: For each answer, calculate the score and insert into the score table
        for question_id, user_answer in answers:
            # Check if the score entry already exists
            cursor.execute("""SELECT * FROM score WHERE question_id = %s AND block_id = %s AND stud_id = %s""",
                           (question_id, block_id, user_id))
            existing_score = cursor.fetchone()

            if existing_score:
                print(f"This question was already attempted before. Scores will not be updated.")
                continue  # Skip to the next question

            # Fetch the correct answer for the question
            cursor.execute("""SELECT correct_answer FROM question WHERE question_id = %s""", (question_id,))
            correct_answer_data = cursor.fetchone()

            if not correct_answer_data:
                print(f"No correct answer found for question {question_id}")
                continue

            correct_answer = correct_answer_data[0]
            # Calculate score: 3 for correct, 1 for incorrect
            score = 3 if user_answer == correct_answer else 1

            # Step 4: Insert the score for the question if it doesn't exist
            timestamp = datetime.datetime.now()  # Get the current timestamp
            cursor.execute("""INSERT INTO score (course_id, textbook_id, chapter_id, section_id, block_id,
                                                  activity_id, question_id, score, timestamp, stud_id)
                              VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                           (course_id, textbook_id, chapter_id, section_id, block_id, activity_id, question_id,
                            score, timestamp, user_id))

            # No need to call fetchall() after INSERT
            # It's only required for SELECT queries that expect results

        # Commit the changes to the database
        reservationConnection.commit()
        print("Scores submitted successfully.")

    except mysql.connector.Error as err:
        print('Error:', err)
    finally:
        cursor.close()
        reservationConnection.close()


def view_block(user_id, course_id, chapter_id, section_id):
    # Connect to the database
    reservationConnection, cursor = connectDB()
    if not cursor:
        return

    try:
        print("\n--- View Block ---")

        # Step 1: Fetch the textbook_id from the course table using the course_id
        cursor.execute("""SELECT textbook_id FROM course WHERE course_id = %s""", (course_id,))
        course_data = cursor.fetchone()

        if not course_data:
            print("Invalid course_id. Course not found.")
            return

        textbook_id = course_data[0]
        print(f"Using textbook_id: {textbook_id}")

        # Ensure previous results are discarded
        cursor.fetchall()  # Discards any remaining results from the previous query

        # Step 2: Get the block details based on the textbook_id, chapter_id, and section_id
        cursor.execute("""SELECT block_id, is_type FROM content_block
                          WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s""",
                       (textbook_id, chapter_id, section_id))
        block = cursor.fetchone()

        if not block:
            print("No block found for the given textbook, chapter, and section.")
            return

        block_id, block_type = block

        # Ensure previous results are discarded
        cursor.fetchall()  # Discards any remaining results from the previous query

        # Step 3: Display content based on block type
        print(f"\nBlock Content for Block ID {block_id}:")

        if block_type == 'text':
            # Fetch content from the text table for text blocks
            cursor.execute("""SELECT text_content FROM text
                              WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s AND block_id = %s""",
                           (textbook_id, chapter_id, section_id, block_id))
            text_content = cursor.fetchone()
            if text_content:
                print(text_content[0])  # Show the text content
            else:
                print("No text content found.")

            # Display options after text content
            print("\nMenu:")
            print("1. Next")
            print("2. Go back")
            choice = input("Choose an option (1-2): ")

            if choice == '1':
                student_landing_page(user_id)  # Go back to the landing page
            elif choice == '2':
                view_section(user_id)  # Go back to the view_section page
            else:
                print("Invalid choice. Please enter a valid option.")
                return

        elif block_type == 'picture':
            # Fetch content from the image table for image blocks
            cursor.execute("""SELECT image_content, alt_text FROM image
                              WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s AND block_id = %s""",
                           (textbook_id, chapter_id, section_id, block_id))
            image_content = cursor.fetchone()
            if image_content:
                print(f"Image: {image_content[0]}")  # Show image content (filename)
                print(f"Alt text: {image_content[1]}")  # Show alt text for the image
            else:
                print("No image content found.")

            # Display options after image content
            print("\nMenu:")
            print("1. Next")
            print("2. Go back")
            choice = input("Choose an option (1-2): ")

            if choice == '1':
                student_landing_page(user_id)  # Go back to the landing page
            elif choice == '2':
                view_section(user_id)  # Go back to the view_section page
            else:
                print("Invalid choice. Please enter a valid option.")
                return

        elif block_type == 'activity':
            # Fetch activity questions
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

                print(f"\n{question_text}")  # Display question text
                print(f"1. {option1}")
                print(f"2. {option2}")
                print(f"3. {option3}")
                print(f"4. {option4}")
                user_answer = input("Choose the correct option (1-4): ")

                # Show the explanation for the selected option immediately
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

                # Collect the answers
                answers.append((question_id, user_answer))

            # Show the options for next/submit
            print("\nMenu:")
            print("1. Next/Submit")
            print("2. Back")
            choice = input("Choose an option (1-2): ")

            if choice == '1':
                submit_answers(user_id, textbook_id, chapter_id, section_id, block_id, answers)
                print("Answers submitted successfully.")
                student_landing_page(user_id)  # Go back to the landing page
            elif choice == '2':
                print("Going back to the section.")
                view_section(user_id)  # Go back to the view_section page
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
