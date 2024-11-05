from pathlib import Path
from aifc import Error
from db_utils import connectDB
import sys
sys.path.append('/Users/apurv/NCSU/Fall24_Sem3/DBMS/project/e-learning-platform/flow/admin/')
import admin_flow
def ta_flow(ta_id):
    conn, cursor = connectDB()
    while(True):
        print("\nWelcome to TA Landing Page.")
        print("1. Go to Active Course")
        print("2. View Courses")
        print("3. Change Password")
        print("4. Logout")

        choice = input("Choose Option: ")
        if choice == '1': #Go to Active Course
            active_course(ta_id)
        elif choice == '2': #Handle View Courses
            _, cursor = connectDB()
            get_course = f"SELECT course_id FROM teaching_assistant WHERE ta_id = '{ta_id}'"
            cursor.execute(get_course)
            result = cursor.fetchone()
            if result:
                print(f"TAID: {ta_id}, CourseID: {result[0]}")
            else:
                print("Failed to find course id.")
                return
        elif choice == '3': #Change Password
            current = input("Enter current password: ")
            get_pass = f"SELECT password FROM user WHERE ta_id = '{ta_id}' AND role = '4'"
            cursor.execute(get_pass)
            result = cursor.fetchone()
            # print(result)
            if not result or current != result[0]:
                print("Failed to verify current password.")
                continue
            print("1. Update")
            print("2. Go Back")
            op = input("Choose Option: ")
            if op == "1": #Update
                while(True):
                    new_pass = input("Enter New Password: ")
                    confirm_pass = input("Confirm New Password: ")
                    if new_pass != confirm_pass:
                        print("Failed to confirm new password.\n")
                        continue
                    else:
                        try:
                            query = f"UPDATE user SET password = '{new_pass}' WHERE ta_id = '{ta_id}'"
                            cursor.execute(query)
                            conn.commit()
                            print("Success: Password Changed.")
                            break
                        except Error as e:
                            print("Failed to change the password.")
                            print(f"An error occurred: {e}")
                            current_filename = Path(__file__).name
                            print(f"Error executing SQL in {current_filename}: {e}")
                            return False
                        
            elif op == "2": #Go Back
                continue

        elif choice == '4': #Logout
            return
            


def active_course(ta_id):
    _, cursor = connectDB()
    
    while True:
        course_id = input("Provide Course ID: ")
        print("1. View Students.")
        print("2. Add New Chapter.")
        print("3. Modify Chapters.")
        print("4. Go Back.")
        choice = input("Choose Option: ")
        
        if choice == "1":
            get_students = f"SELECT stud_id FROM enroll WHERE course_id = '{course_id}'"
            cursor.execute(get_students)
            result = cursor.fetchall()
            if result:
                print(result)
            else:
                print("Data Not Found.")
        
        elif choice == "2":
            get_textbook_it = f"SELECT textbook_id FROM course WHERE course_id = '{course_id}'"
            cursor.execute(get_textbook_it)
            result = cursor.fetchone()
            if result:
                textbook_id = result[0]
            
            admin_flow.create_chapter_page(ta_id,textbook_id)
        elif choice == "3":
            modify_chapters()
            
def modify_chapters():
    print("aa")