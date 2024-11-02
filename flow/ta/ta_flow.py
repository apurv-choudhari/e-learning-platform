from pathlib import Path
from aifc import Error
from db_utils import connectDB

def ta_flow(userid):
    conn, cursor = connectDB()
    while(True):
        print("\nWelcome to TA Landing Page.")
        print("1. Go to Active Course")
        print("2. View Courses")
        print("3. Change Password")
        print("4. Logout")

        choice = input("Choose Option: ")
        if choice == '1': #Go to Active Course
            active_course()
        elif choice == '3': #Change Password
            current = input("Enter current password: ")
            get_pass = f"SELECT password FROM user WHERE user_id = '{userid}' AND role = '4'"
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
                            query = f"UPDATE user SET password = '{new_pass}' WHERE user_id = '{userid}'"
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
            
        return


def active_course():
    print("1. View Students.")
    print("2. Add New Chapter.")
    print("3. Modify Chapters.")
    print("4. Go Back.")
    
    