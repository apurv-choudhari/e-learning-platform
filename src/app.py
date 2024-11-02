
from db_utils import connectDB
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flow.admin import admin_flow
from flow.faculty import faculty_flow
from flow.student import student_flow
from flow.ta import ta_flow
from utils.validate_credentials import login_flow

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
        print("5. Exit")
        choice = input("Enter Choice (1-5): ")
        
        if choice not in {'1', '2', '3', '4', '5'}:
            print("Invalid choice. Please enter a number between 1 and 5.")

        if choice == '5':
            print("Exiting the application.")
            sys.exit()
        user_id = input("User ID: ")
        password = input("Password: ")
        if choice == '1':
            if login_flow(choice):
                admin_flow.admin_flow(choice, user_id, password)
        elif choice == '2':
            if login_flow(choice, user_id, password):
                faculty_flow.faculty_flow()
        elif choice == '3':
            print("1. Enroll In a Course.")
            print("2. Sign-In")
            print("3. Go Back")
            op = input("Choose Option: ")
            if op == "1":
                print("Handle Enrollemnt Request")
            elif op == "2":
               if login_flow(choice, user_id, password):
                    student_flow.student_flow()
            elif op == "3":
                continue
        elif choice == '4':
            if login_flow(choice, user_id, password):
                ta_flow.ta_flow(user_id)

if __name__ == "__main__":
    _, cursor = connectDB()
    main_menu()
