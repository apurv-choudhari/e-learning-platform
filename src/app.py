
from db_utils import connectDB
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flow.admin import admin_flow
from flow.faculty import faculty_flow
from flow.student import student_flow
from flow.ta import ta_flow

cursor = None

role_mapping = {
    1:"Admin",
    2:"Faculty",
    3:"Student",
    4:"TA"
}

def signin(role):
    
    while(True):
        userid = input("User ID: ")
        password = input("Password: ")
        print(f"\n {role_mapping[role]} Please Select Option: ")
        print("1. Sign-In")
        print("2. Go Back")

        choice = input("Enter Choice (1,2): ")
        if choice == '2':
            return False
        elif choice == '1':
            query = f"SELECT password FROM user WHERE user_id = '{userid}' AND role_no = '{role}'"
            cursor.execute(query)
            result = cursor.fetchone()
            # print(result)
            if result and password == result[0]:
                print("Login Successful")
                return True
            
            print("Login Failed. Try Again.\n")

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
        
        if int(choice) not in range(1,6):
            print("Invalid choice. Please enter a number between 1 and 5.")

        if choice == '5':
            print("Exiting the application.")
            sys.exit()

        if choice == '1':
            if signin(int(choice)) == True:
                admin_flow.admin_flow()
        elif choice == '2':
            if signin(int(choice)) == True:
                faculty_flow.faculty_flow()
        elif choice == '3':
            print("1. Enroll In a Course.")
            print("2. Sign-In")
            print("3. Go Back")
            op = input("Choose Option: ")
            if op == "1":
                print("Handle Enrollemnt Request")
            elif op == "2":
                if signin(int(choice)) == True:
                    student_flow.student_flow()
            elif op == "3":
                continue
        elif choice == '4':
            if signin(int(choice)) == True:
                ta_flow.ta_flow()

if __name__ == "__main__":
    _, cursor = connectDB()
    main_menu()
