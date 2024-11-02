from utils.validate_credentials import login_flow

def admin_login():
    while True:
        print("\nAdmin Login:")
        if not login_flow(role = 1):
            break
        print("\n1. Option 1")
        print("2. Go Back")
        choice = input("Enter Choice (1-2): ")

        if choice == '1':
            print("Admin Option 1")
            # Admin landing page or further menu logic here
        elif choice == '2':
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")
