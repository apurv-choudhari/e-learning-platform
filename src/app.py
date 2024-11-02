
from main import connectDB
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flow.admin import admin_flow
from flow.faculty import faculty_flow
from flow.student import student_flow
from flow.ta import ta_flow

def main_menu():
    print("Welcome to ZyBooks Terminal Application")
    while True:
        print("\nMain Menu:")
        print("1. Admin Login")
        print("2. Faculty Login")
        print("3. TA Login")
        print("4. Student Login")
        print("5. Exit")

        choice = input("Enter Choice (1-5): ")
        
        if choice == '1':
            admin_flow.admin_login()
        elif choice == '2':
            faculty_flow.faculty_login()
        elif choice == '3':
            ta_flow.ta_login()
        elif choice == '4':
            student_flow.student_login()
        elif choice == '5':
            print("Exiting the application.")
            sys.exit()
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main_menu()
