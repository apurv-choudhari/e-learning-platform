import sys
from pathlib import Path
import mysql.connector
import os
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from . import ta_queries as ta_db
from ..admin import admin_flow
from ..admin import admin_db_utils as admin_db
from ..faculty import faculty_db_utils as fac_db

def ta_flow(ta_id):
    while True:
        print("\nWelcome to TA Landing Page.")
        print("1. Go to Active Course")
        print("2. View Courses")
        print("3. Change Password")
        print("4. Logout")

        choice = input("Choose an option: ")

        if choice == '1':
            goto_active_course(ta_id)
        elif choice == '2':
            result = ta_db.get_course_id(ta_id)
            if result:
                print(f"TA ID: {ta_id}, Course ID: {result[0]}")
            else:
                print("No course found.")
        elif choice == '3':
            change_password(ta_id)
        elif choice == '4':
            return

def goto_active_course(ta_id):
    course_id = input("Provide Course ID: ")
    while True:
        print("\n1. View Students")
        print("2. Add New Chapter")
        print("3. Modify Chapters")
        print("4. Go Back")

        choice = input("Choose an option: ")

        if choice == "1":
            students = ta_db.get_students(course_id)
            print(students if students else "No students found.")
        elif choice == "2":
            add_chapter(ta_id, course_id)
            # result = ta_db.get_textbook_id(course_id)
            # if result:
            #     admin_flow.create_chapter_page(ta_id, result[0])
        elif choice == "3":
            if modify_chapter(ta_id, course_id) == "landing_page":
                return "landing_page"
        elif choice == "4":
            return

########### Modify Chapters ################

def modify_chapter(user_id, course_id):
    print("\nTA: Modify Chapter")
    chapter_id = input("Enter the unique Chapter ID: ")
    while True:
        print(f"You are viewing Chapter - {chapter_id}")
        print("\nMenu")
        print("1. Add New Section")
        print("2. Modify Section")
        print("3. Go Back")
        choice = input("Enter choice (1-3): ")

        match choice:
            case '1':
                print("\nRedirecting to Add New Section...")
                add_new_section(user_id, course_id, chapter_id)
            case '2':
                print("\nRedirecting to Modify Section...")
                if modify_section(user_id, course_id, chapter_id) == "landing_page":
                    return "landing_page"
            case '3':
                print("\nRedirecting to previous page...")
                return
            case _:
                print("Invalid choice. Please enter 1-5")
    return

def modify_section(user_id, course_id, chapter_id):
    print("\nTA: Modify Section")
    section_id = input("Enter the Section no: ")
    while True:
        print(f"You are viewing Section - {section_id}")
        print("1. Add New Content Block")
        print("2. Modify Content Block")
        print("3  Delete Content Block")
        print("4. Hide Content Block")
        print("5. Go Back")
        choice = input("Enter choice (1-5): ")

        match choice:
            case '1':
                print("\nRedirecting to Add New Content Block...")
                add_content_block(user_id, course_id, chapter_id, section_id)
            case '2':
                print("\nRedirecting to Modify Content Block...")
                if modify_content_block(user_id, course_id, chapter_id, section_id) == "landing_page":
                    return "landing_page"
            case '3':
                print("\nRedirecting to Delete Content Block...")
                delete_content_block(user_id, course_id, chapter_id, section_id)
            case '4':
                print("\nRedirecting to Hide Content Block...")
                hide_content_block(user_id, course_id, chapter_id, section_id)
            case '5':
                print("\nRedirecting to previous page...")
                return
            case _:
                print("Invalid choice. Please enter 1 - 5")
    return


def hide_content_block(user_id, course_id, chapter_id, section_id):
    print("\nTA: Hide Content Block")
    block_id = input("Enter the Content Block id: ")
    while True:
        print("\n Menu")
        print("1. Hide")
        print("2. Go Back")

        choice = input("Enter choice (1-2): ")
        match choice:
                case '1':
                    print("Hiding...")
                    ta_db.hide_content_block_util(user_id, course_id, chapter_id, section_id, block_id)
                case '2':
                    print("\nRedirecting to Previous page")
                    return
                case _:
                    print("Invalid choice. Please enter 1 or 2")

def delete_content_block(user_id, course_id, chapter_id, section_id):
    print("\nTA: Delete Content Block")
    block_id = input("Enter the Content Block id:")
    while True:
        print("\n Menu")
        print("1. Delete")
        print("2. Go Back")

        choice = input("Enter choice (1-2): ")
        
        match choice:
            case '1':
                print("Deleting...")
                ta_db.del_content_block(user_id, course_id, chapter_id, section_id, block_id)
            case '2':
                print("\nRedirecting to Previous page")
                return
            case _:
                print("Invalid choice. Please enter 1 or 2")

def modify_content_block(user_id, course_id, chapter_id, section_id):
    print("\nTA: Modify Content Block")
    block_id = input("Provide Content Block ID: ")
    while True:
        print(f"You are viewing Block - {block_id}")
        print("\nMenu:")
        print("1. Add Text")
        print("2. Add Picture")
        print("3. Add Activity")
        print("4. Go Back")
        print("5. Landing Page")
        choice = input("Enter choice (1-4): ")

        match choice:
            case '1':
                content_type = 'text'
                if ta_db.insert_content_block(user_id, course_id, chapter_id, section_id, block_id, content_type):
                    print("\nRedirecting to Add Text...")
                    add_text(user_id, course_id, chapter_id, section_id, block_id)
                else: return
                    
            case '2':
                content_type = 'image'
                if ta_db.insert_content_block(user_id, course_id, chapter_id, section_id, block_id, content_type):
                    print("\nRedirecting to Add Picture...")
                    add_picture(user_id, course_id, chapter_id, section_id, block_id)
                else: return
            case '3':
                content_type = 'activity'
                if ta_db.insert_content_block(user_id, course_id, chapter_id, section_id, block_id, content_type):
                    print("\nRedirecting to Add Activity...")
                    add_activity(user_id, course_id, chapter_id, section_id, block_id)
                else: return
            case '4':
                print("\nRedirecting to Previous page...")
                return
            case '5':
                return "landing_page"
            case _:
                print("Invalid choice. Please enter 1 - 4")
    return
########### Modify Chapters ################


########### ADD CHAPTER #####################
def add_chapter(user_id, course_id):
    print("\nTA: Add New Chapter")
    chapter_id = input("Provide Chapter ID: ")
    chapter_title = input("Enter the Chapter Title: ")

    if ta_db.insert_chapter(user_id, course_id, chapter_id, chapter_title):
        while True:
            print(f"You are viewing Chapter - {chapter_id}")
            print("\nMenu:")
            print("1. Add New Section")
            print("2. Go Back")
            choice = input("Enter choice (1-2): ")

            match choice:
                case '1':
                    print("Redirecting to Add New Section page...")
                    add_new_section(user_id, course_id, chapter_id)
                case '2':
                    print("Returning to previous page...")
                    return False
                case _:
                    print("Invalid choice. Please enter 1 or 2")
    else:
        print("Failed to create chapter. Please check the details and try again.")
        return False
    

def add_new_section(user_id, course_id, chapter_id):
    print("\nTA: Add New Section")
    section_id = input("Provide Section ID: ")
    section_title = input("Enter the Section Title: ")

    if ta_db.insert_section(course_id, chapter_id, section_id, section_title, user_id):
        while True:
            print(f"You are viewing Section - {section_id}")
            print("\nMenu:")
            print("1. Add New Content Block")
            print("2. Go Back")
            choice = input("Enter choice (1-2): ")

            match choice:
                case '1':
                    print("Redirecting to Add New Content Block")
                    add_content_block(user_id, course_id, chapter_id, section_id)
                case '2':
                    print("Returning to previous page...")
                    return
                case _:
                    print("Invalid choice. Please enter 1 or 2")
    else:
        print("Failed to add section. Please check the details and try again.")
        return

def add_content_block(user_id, course_id, chapter_id, section_id):
    print("\nTA: Add New Content Block")
    block_id = input("Provide Content Block ID: ")
    while True:
        print(f"You are viewing Block - {block_id}")
        print("\nMenu:")
        print("1. Add Text")
        print("2. Add Picture")
        print("3. Add Activity")
        print("4. Hide Activity")
        print("5. Go Back")
        choice = input("Enter choice (1-4): ")

        match choice:
            case '1':
                content_type = 'text'
                if ta_db.insert_content_block(user_id, course_id, chapter_id, section_id, block_id, content_type):
                    print("\nRedirecting to Add Text...")
                    add_text(user_id, course_id, chapter_id, section_id, block_id)
                else: return
                    
            case '2':
                content_type = 'image'
                if ta_db.insert_content_block(user_id, course_id, chapter_id, section_id, block_id, content_type):
                    print("\nRedirecting to Add Picture...")
                    add_picture(user_id, course_id, chapter_id, section_id, block_id)
                else: return
            case '3':
                content_type = 'activity'
                if ta_db.insert_content_block(user_id, course_id, chapter_id, section_id, block_id, content_type):
                    print("\nRedirecting to Add Activity...")
                    add_activity(user_id, course_id, chapter_id, section_id, block_id)
                else: return
            case '4':
                print("\nRedirecting to Hide Activity page...")
                ta_db.hide_activity(user_id, course_id, chapter_id, section_id, block_id)
                return
            case '5':
                print("\nRedirecting to Previous page...")
                return
            case _:
                print("Invalid choice. Please enter 1 - 4")
    return

def add_text(user_id, course_id, chapter_id, section_id, block_id):
    print("\nTA: Add Text")
    text_content = input("Enter the text to be added: ")
    textbook_id = ta_db.get_textbook_id_for_ta(course_id, user_id)
    text_id = admin_db.get_next_text_id(textbook_id, chapter_id, section_id, block_id)
    while True:
        print("\nMenu:")
        print("1. Add")
        print("2. Go Back")
        choice = input("Enter choice (1-2): ")

        match choice:
            case '1':
                if fac_db.insert_text(textbook_id, chapter_id, section_id, block_id, text_id, text_content):
                    print("Text added successfully.")
                    return
                else:
                    print("Failed to add text. Please try again.")
                    return
            case '2':
                return
            case _:
                print("Invalid choice. Please enter 1 or 2.")
    return

def add_picture(user_id, course_id, chapter_id, section_id, block_id):
    print("\nTA: Add Picture")
    image_content = input("Enter the Picture (image URL): ")
    alt_text = input("Enter Alt Text: ")

    textbook_id = ta_db.get_textbook_id_for_ta(course_id, user_id)
    image_id = admin_db.get_next_image_id(textbook_id, chapter_id, section_id, block_id)

    while True:
        print("\nMenu:")
        print("1. Add")
        print("2. Go Back")
        choice = input("Enter choice (1-2): ")

        match choice:
            case '1':
                if fac_db.insert_image(textbook_id, chapter_id, section_id, block_id, image_id, image_content, alt_text):
                    print("Picture added successfully.")
                    return
                else:
                    print("Failed to add picture. Please try again.")
            case '2':
                return
            case _:
                print("Invalid choice. Please enter 1 or 2")
    return

def add_activity(user_id, course_id, chapter_id, section_id, block_id):
    print("\nTA: Add Activity")
    activity_id = input("Provide Activity ID: ")

    textbook_id = ta_db.get_textbook_id_for_ta(course_id, user_id)

    if fac_db.insert_activity(textbook_id, chapter_id, section_id, block_id, activity_id, user_id):
        while True:
            print("\nMenu:")
            print(f"You are viewing Activity - {activity_id}")
            print("1. Add Question")
            print("2. Go Back")
            choice = input("Enter choice (1-2): ")

            match choice:
                case '1':
                    add_question(user_id, course_id, chapter_id, section_id, block_id, activity_id)
                case '2':
                    return
                case _:
                    print("Invalid choice. Please enter 1 or 2")
    else:
        print("Failed to create activity. Please check the details and try again.")

def add_question(user_id, course_id, chapter_id, section_id, block_id, activity_id):
    print("\nTA: Add Question")
    question_id = input("Enter Question ID: ")
    question_text = input("Enter Question Text: ")
    options = []
    for i in range(1, 5):
        option_text = input(f"Enter Option {i} Text: ")
        option_explanation = input(f"Enter Option {i} Explanation: ")
        options.append((option_text, option_explanation))

    correct_answer = int(input(f"Enter the correct option ? (1/2/3/4): "))

    if correct_answer is None:
        print("Error: At least one option must be marked as correct.")
        return
    
    textbook_id = ta_db.get_textbook_id_for_ta(course_id, user_id)
    while True:
        print("\nMenu:")
        print("1. Save")
        print("2. Cancel")
        choice = input("Enter choice (1-2): ")

        match choice:
            case '1':
                if fac_db.insert_question(textbook_id, chapter_id, section_id, block_id, activity_id, question_id, question_text, options, correct_answer, user_id):
                    print("Question added successfully.")
                    break
                else:
                    print("Failed to add question. Please try again.")
            case '2':
                return
            case _:
                print("Invalid choice. Please enter 1 or 2")
    
########### ADD CHAPTER #####################

def change_password(ta_id):
    current = input("Enter current password: ")
    password = ta_db.get_password(ta_id, "4")
    if not password or current != password[0]:
        print("Failed to verify current password.")
        return False

    print("1. Update")
    print("2. Go Back")
    option = input("Choose an option: ")

    if option == "1":  # Update password
        while True:
            new_pass = input("Enter new password: ")
            confirm_pass = input("Confirm new password: ")
            if new_pass != confirm_pass:
                print("Passwords do not match.\n")
                continue
            try:
                ta_db.update_password(ta_id, new_pass)
                print("Password changed successfully.")
                break
            except mysql.connector.Error as e:
                print(f"Failed to change the password: {e}")
                return False
    elif option == "2":  # Go Back
        return False

# def modify_chapters(user_id, role, course_id):
#     if role == "1":  # FOr Admin
#         modify_chapters_Admin()
#     elif role == "4":  # For TA
#         modify_chapters_TA(user_id, course_id)


def modify_chapters_Admin():
    chapter_id = input("Provide Chapter ID: ")
    print("1. Add New Section")
    print("2. Add New Activity")
    print("3. Go Back")

def modify_chapters_TA(user_id, course_id):
    chapter_id = input("Provide Chapter ID: ")
    print("1. Add New Section")
    print("2. Add New Activity")
    print("3. Go Back")

    choice = input("Choose an option: ")

    result = ta_db.get_textbook_id_for_ta(course_id, user_id)
    if not result:
        print("No textbook found for the specified TA and course.")
        return

    textbook_id = result[0]

    if choice == "1":
        admin_flow.create_section_page(user_id, textbook_id, chapter_id)
    elif choice == "2":
        section_id = input("Provide Section ID: ")
        block_result = ta_db.get_content_block_id(textbook_id, chapter_id, section_id)
        if block_result:
            admin_flow.add_activity_page(user_id, textbook_id, chapter_id, section_id, block_result[0])
        else:
            print("No content block found.")
