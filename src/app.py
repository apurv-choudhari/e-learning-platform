from db_utils import connectDB
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flow.admin import admin_flow
from flow.faculty import faculty_flow
from flow.student import student_flow
from flow.ta import ta_flow
from utils.validate_credentials import login_flow
from test_queries import test_user_queries

cursor = None

role_mapping = {
    1:"Admin",
    2:"Faculty",
    3:"Student",
    4:"TA"
}

def main_menu():
    print("Welcome to ZyBooks Terminal Application")
    while True:
        print("\nMain Menu:")
        print("1. Admin Login")
        print("2. Faculty Login")
        print("3. Student Login")
        print("4. TA Login")
        print("5. Test Queries")
        print("6. Exit")
        choice = input("Enter Choice (1-5): ")
        
        if choice not in {'1', '2', '3', '4', '5'}:
            print("Invalid choice. Please enter a number between 1 and 5.")

        if choice == '6':
            print("Exiting the application.")
            sys.exit()

        if choice == '1':
            user_id, login_success = login_flow(choice)
            if login_success:
                admin_flow.admin_flow(user_id)
        elif choice == '2':
            user_id, login_success = login_flow(choice)
            if login_success:
                faculty_flow.faculty_flow(user_id)
        elif choice == '3':
            print("1. Enroll In a Course.")
            print("2. Sign-In")
            print("3. Go Back")
            op = input("Choose Option: ")
            if op == "1":
                student_flow.enroll_in_course()
            elif op == "2":
                user_id, login_success = login_flow(3)
                if login_success:
                    student_flow.student_landing_page(user_id)
            elif op == "3":
                continue
        elif choice == '4':
            user_id, login_success = login_flow(choice)
            if login_success:
                ta_flow.ta_flow(user_id)
        elif choice == '5':
            test_user_queries()

if __name__ == "__main__":
    _, cursor = connectDB()
    main_menu()
