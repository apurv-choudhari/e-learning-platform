from db_utils import connectDB

def ta_flow():
    cursor = connectDB()
    while(True):
        print("\nWelcome to TA Landing Page.")
        print("1. Go to Active Course")
        print("2. View Courses")
        print("3. Change Password")
        print("4. Logout")

        choice = input("Choose Option: ")
        if choice == '1':
            print("A")
        elif choice == '3':
            current = input("Enter current password: ")
            print("1. Update")
            print("2. Go Back")
            op = input("Choose Option: ")
            if op == "1":
                while(True):
                    new = input("Enter New Password: ")
                    confirm = input("Confirm New Password: ")
                    if new != confirm:
                        print("Failed to confirm new password.")
                        continue
                    # else:
                        
            elif op == "2":
                continue

        elif choice == '4':
            return
            
        return
