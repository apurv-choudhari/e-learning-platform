import sys
from pathlib import Path
import mysql.connector
import os
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from . import ta_queries
from ..admin import admin_flow


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
            result = ta_queries.get_course_id(ta_id)
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
            students = ta_queries.get_students(course_id)
            print(students if students else "No students found.")
        elif choice == "2":
            result = ta_queries.get_textbook_id(course_id)
            if result:
                admin_flow.create_chapter_page(ta_id, result[0])
        elif choice == "3":
            modify_chapters(ta_id, "4", course_id)
        elif choice == "4":
            return

def change_password(ta_id):
    current = input("Enter current password: ")
    password = ta_queries.get_password(ta_id, "4")
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
                ta_queries.update_password(ta_id, new_pass)
                print("Password changed successfully.")
                break
            except mysql.connector.Error as e:
                print(f"Failed to change the password: {e}")
                return False
    elif option == "2":  # Go Back
        return False

def modify_chapters(user_id, role, course_id):
    if role == "4":  # For TA
        modify_chapters_TA(user_id, course_id)

def modify_chapters_TA(user_id, course_id):
    chapter_id = input("Provide Chapter ID: ")
    print("1. Add New Section")
    print("2. Add New Activity")
    print("3. Go Back")

    choice = input("Choose an option: ")

    result = ta_queries.get_textbook_id_for_ta(user_id, course_id)
    if not result:
        print("No textbook found for the specified TA and course.")
        return

    textbook_id = result[0]

    if choice == "1":
        admin_flow.create_section_page(user_id, textbook_id, chapter_id)
    elif choice == "2":
        section_id = input("Provide Section ID: ")
        block_result = ta_queries.get_content_block_id(textbook_id, chapter_id, section_id)
        if block_result:
            admin_flow.add_activity_page(user_id, textbook_id, chapter_id, section_id, block_result[0])
        else:
            print("No content block found.")
