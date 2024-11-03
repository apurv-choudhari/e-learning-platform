# from utils.validate_credentials import login_flow

# def student_flow(user_id):
#     print("Student Landing Page.")
#     return


from db_utils import connectDB
from utils.validate_credentials import login_flow

def student_flow(user_id):
    while True:
        print("\nWelcome to Student Main Menu:")
        print("1. Enroll in a Course")
        print("2. Sign-In")
        print("3. Go Back")
        choice = input("Choose an option (1-3): ")

        if choice == '1':
            enroll_in_course()
        elif choice == '2':
            sign_in_flow(user_id)  # Pass user_id to sign_in_flow
        elif choice == '3':
            print("Returning to the main menu.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def enroll_in_course():
    print("\n--- Enroll in a Course ---")
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    email = input("Enter Email: ")
    course_token = input("Enter Course Token: ")

    print("\n1. Enroll")
    print("2. Go Back")
    choice = input("Choose an option (1-2): ")

    if choice == '1':
        # Code to create account and add student to waiting list
        print("Enrollment request recorded. Account created if this is the first request.")
    elif choice == '2':
        print("Returning to Student Main Menu.")
    else:
        print("Invalid choice. Returning to Student Main Menu.")

def sign_in_flow(user_id):
    user_id, login_success = login_flow(3)

    if login_success:
        student_landing_page(user_id)
    else:
        print("Invalid credentials, returning to student main menu")

def student_landing_page(user_id):
    while True:
        print("\n--- Student Landing Page ---")
        print("1. View a Section")
        print("2. View Participation Activity Points")
        print("3. Logout")
        choice = input("Choose an option (1-3): ")

        if choice == '1':
            view_section()
        elif choice == '2':
            view_participation_points(user_id)
        elif choice == '3':
            print("Logging out.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def view_section():
    chapter_id = input("Enter Chapter ID: ")
    section_id = input("Enter Section ID: ")

    print("\n1. View Block")
    print("2. Go Back")
    choice = input("Choose an option (1-2): ")

    if choice == '1':
        view_block()
    elif choice == '2':
        print("Returning to Student Landing Page.")
    else:
        print("Invalid choice. Returning to Student Landing Page.")

def view_block():
    print("\n--- Viewing Block ---")
    block_type = input("Is this a Content block or an Activity block? (Enter 'content' or 'activity'): ")

    if block_type.lower() == 'content':
        print("Displaying content. Press 1 for Next, 2 to Go Back.")
        choice = input("Choose an option (1-2): ")
        if choice == '1':
            print("Proceeding to the next block.")
        elif choice == '2':
            print("Returning to previous page.")
    elif block_type.lower() == 'activity':
        answer = input("Enter the ID of the correct answer (1-4): ")
        print("\n1. Next/Submit")
        print("2. Go Back")
        choice = input("Choose an option (1-2): ")
        if choice == '1':
            print("Answer submitted. Moving to the next block.")
        elif choice == '2':
            print("Returning to previous page.")
    else:
        print("Invalid block type. Returning to Student Landing Page.")

def view_participation_points(user_id):
    # Assuming a function to fetch and display participation points
    participation_points = 100  # Placeholder value
    print(f"Your current participation activity points: {participation_points}")
    input("Press any key to return to the Student Landing Page.")
