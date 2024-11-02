from flow.admin.admin_db_utils import insert_user, insert_textbook

def admin_flow(user_id):
    print("Admin: Landing Page. Welcome, " + user_id + "!")
    while True:
        print("\nAdmin Menu:")
        print("1. Create a Faculty Account")
        print("2. Create E-textbook")
        print("3. Modify E-textbooks")
        print("4. Create New Active Course")
        print("5. Create New Evaluation Course")
        print("6. Logout")
        
        choice = input("Enter choice (1-6): ")

        match choice:
            case '1':
                create_faculty_page()
            case '2':
                create_textbook()
            case '3':
                print("\nRedirecting to Modify E-textbooks page...")
            case '4':
                print("\nRedirecting to Create New Active Course page...")
            case '5':
                print("\nRedirecting to Create New Evaluation Course page...")
            case '6':
                print("\nLogging out...")
                break
            case _:
                print("\nInvalid choice. Please enter a number between 1 and 6.")


def create_faculty_page():
    print("\nAdmin: Create a Faculty Account")
    user_id = input("Enter Username: ")
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    email = input("Enter Email: ")
    password = input("Enter Password: ")

    while True:
        print("\nMenu:")
        print("1. Add User")
        print("2. Go Back")
        choice = input("Enter choice (1-2): ")

        match choice:
            case '1':
                insert_user(user_id, first_name, last_name, email, password, 2)
                return
            case '2':
                return
            case _:
                print("Invalid choice. Please enter 1 or 2.")

def create_textbook():
    print("\nAdmin: Create E-textbook")
    title = input("Enter the title of the new E-textbook: ")
    textbook_id = input("Enter the unique E-textbook ID: ")

    insert_textbook()

    while True:
        print("\nMenu:")
        print("1. Add New Chapter")
        print("2. Go Back")
        choice = input("Enter choice (1-2): ")

        match choice:
            case '1':
                create_chapter(textbook_id)
            case '2':
                print("Returning to Admin Landing Page...")
                return
            case _:
                print("Invalid choice. Please enter 1 or 2.")

def create_chapter(textbook_id):
    print('Create new chapter menu')
    return False