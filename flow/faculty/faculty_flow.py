from utils.validate_credentials import login_flow

def faculty_login():
    while True:
        print("\nFaculty Login:")
        if not login_flow(role = 3):
            break

        print("\n1. Option 1")
        print("2. Go Back")
        choice = input("Enter Choice (1-2): ")

        if choice == '1':
            print("Faculty Option 1")
            # Faculty-specific menu logic here
        elif choice == '2':
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")
