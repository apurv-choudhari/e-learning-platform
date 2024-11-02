from utils.validate_credentials import login_flow

def student_login():
    while True:
        print("\n1. Enroll in a Course")
        print("2. Sign-In")
        print("3. Go Back")
        choice = input("Enter Choice (1-2): ")

        if choice == '1':
            print("Course enrollment option for Student")
            # Course enrollment logic here
        elif choice == '2':
            print("\nStudent Login:")
            if not login_flow(role = 3):
                break
            # further student logic after login
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 2.")
