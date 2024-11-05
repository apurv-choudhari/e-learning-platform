from flow.admin.admin_db_utils import insert_textbook, insert_chapter, insert_section, insert_content_block, insert_text_content, insert_image_content, insert_user, insert_activity, insert_question,insert_active_course, get_next_text_id, get_next_image_id, get_faculty_list, get_textbook_list
from flow.admin.helpers import validate_integer_input, validate_required_fields, validate_faculty_id, validate_textbook_id
reset = False
def admin_flow(user_id):
    global reset
    print("Admin: Landing Page. Welcome, " + user_id + "!")
    while True:
        reset = False
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
                create_textbook_page(user_id)
            case '3':
                print("\nRedirecting to Modify E-textbooks page...")
            case '4':
                create_active_course_page(user_id)
            case '5':
                print("\nRedirecting to Create New Evaluation Course page...")
            case '6':
                print("\nLogging out...")
                break
            case _:
                print("\nInvalid choice. Please enter a number between 1 and 6.")


def create_faculty_page():
    global reset
    print("\nAdmin: Create a Faculty Account")
    user_id = input("Enter Username: ")
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    email = input("Enter Email: ")
    password = input("Enter Password: ")

    if not validate_required_fields({
        "Username": user_id,
        "First Name": first_name,
        "Last Name": last_name,
        "Email": email,
        "Password": password
    }):
        return

    while True:
        print("\nMenu:")
        print("1. Add User")
        print("2. Go Back")
        choice = input("Enter choice (1-2): ")

        match choice:
            case '1':
                if insert_user(user_id, first_name, last_name, email, password, 2):
                    return
            case '2':
                return
            case _:
                print("Invalid choice. Please enter 1 or 2.")

def create_textbook_page(user_id):
    global reset
    print("\nAdmin: Create E-textbook")
    title = input("Enter the title of the new E-textbook: ")
    textbook_id = validate_integer_input("Enter the unique E-textbook ID (integer): ")

    if not validate_required_fields({
        "E-textbook Title": title,
        "E-textbook ID": textbook_id
    }):
        return

    if not insert_textbook(title, textbook_id, user_id):
        return

    while True:
        print("\nMenu:")
        print("1. Add New Chapter")
        print("2. Go Back")
        choice = input("Enter choice (1-2): ")

        match choice:
            case '1':
                create_chapter_page(user_id, textbook_id)
                if(reset == True):
                    return
            case '2':
                print("Returning to Admin Landing Page...")
                return
            case _:
                print("Invalid choice. Please enter 1 or 2.")

def create_chapter_page(user_id, textbook_id):
    global reset
    print("\nAdmin: Add New Chapter")
    chapter_id = input("Enter the unique Chapter ID: ")
    chapter_title = input("Enter the Chapter Title: ")

    if not validate_required_fields({
        "Chapter ID": chapter_id,
        "Chapter Title": chapter_title
    }):
        return

    if insert_chapter(user_id, textbook_id, chapter_id, chapter_title):
        while True:
            print("\nMenu:")
            print("1. Add New Section")
            print("2. Go Back")
            print("3. Landing Page")
            choice = input("Enter choice (1-3): ")

            match choice:
                case '1':
                    create_section_page(user_id, textbook_id, chapter_id)
                    if(reset == True):
                        return
                case '2':
                    print("Returning to previous page...")
                    return False
                case '3':
                    print("Returning to User Landing Page...")
                    reset = True
                    return
                case _:
                    print("Invalid choice. Please enter 1, 2, or 3.")
    else:
        print("Failed to create chapter. Please check the details and try again.")
        return False

def create_section_page(user_id, textbook_id, chapter_id):
    global reset
    print(f"\nAdding New Section to Chapter ID: {chapter_id} in Textbook ID: {textbook_id}")
    section_id = input("Enter the unique Section ID: ")
    section_title = input("Enter the Section Title: ")

    if not validate_required_fields({
        "Section ID": section_id,
        "Section Title": section_title
    }):
        return

    if insert_section(textbook_id, chapter_id, section_id, section_title, user_id):
        while True:
            print("\nMenu:")
            print("1. Add New Content Block")
            print("2. Go Back")
            print("3. Landing Page")
            choice = input("Enter choice (1-3): ")

            match choice:
                case '1':
                    create_content_block_page(user_id, textbook_id, chapter_id, section_id)
                    if(reset == True):
                        return
                case '2':
                    print("Returning to previous page...")
                    return
                case '3':
                    print("Returning to User Landing Page...")
                    reset = True
                    return
                case _:
                    print("Invalid choice. Please enter 1, 2, or 3.")
    else:
        print("Failed to add section. Please check the details and try again.")

def create_content_block_page(user_id, textbook_id, chapter_id, section_id):
    global reset
    print(f"\nAdmin: Add New Content Block to Section ID: {section_id} in Chapter ID: {chapter_id} and Textbook ID: {textbook_id}")
    block_id = input("Enter the unique Content Block ID: ")
    
    print("\nMenu:")
    print("1. Add Text")
    print("2. Add Picture")
    print("3. Add Activity")
    print("4. Go Back")
    print("5. Landing Page")
    
    choice = input("Enter choice (1-5): ")
    
    content_type = None
    if choice == '1':
        content_type = "text"
        if insert_content_block(textbook_id, chapter_id, section_id, block_id, content_type, user_id):
            add_text_page(user_id, textbook_id, chapter_id, section_id, block_id)
            if(reset == True):
                return
        else:
            print("Failed to add content block.")
    elif choice == '2':
        content_type = "image"
        if insert_content_block(textbook_id, chapter_id, section_id, block_id, content_type, user_id):
            add_image_page(user_id, textbook_id, chapter_id, section_id, block_id)
            if(reset == True):
                return
        else:
            print("Failed to add content block.")
    elif choice == '3':
        content_type = "activity"
        if insert_content_block(textbook_id, chapter_id, section_id, block_id, content_type, user_id):
            add_activity_page(user_id, textbook_id, chapter_id, section_id, block_id)
            if(reset == True):
                return
        else:
            print("Failed to add content block.")
    elif choice == '4':
        print("Going back to the previous page...")
        return
    elif choice == '5':
        print("Returning to User Landing Page...")
        reset = True
        return
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
        return

def add_text_page(user_id, textbook_id, chapter_id, section_id, block_id):
    global reset
    print("\nAdmin: Add Text")
    text_content = input("Enter the Text: ")

    if not validate_required_fields({"Text": text_content}):
        return

    text_id = get_next_text_id(textbook_id, chapter_id, section_id, block_id)

    while True:
        print("\nMenu:")
        print("1. Add")
        print("2. Go Back")
        print("3. Landing Page")
        choice = input("Enter choice (1-3): ")

        match choice:
            case '1':
                if insert_text_content(textbook_id, chapter_id, section_id, block_id, text_id, text_content):
                    print("Text added successfully.")
                    return
                else:
                    print("Failed to add text. Please try again.")
            case '2':
                return
            case '3':
                print("Returning to User Landing Page...")
                reset = True
                return      
            case _:
                print("Invalid choice. Please enter 1, 2, or 3.")


def add_image_page(user_id, textbook_id, chapter_id, section_id, block_id):
    global reset
    print("\nAdmin: Add Picture")
    image_content = input("Enter the Picture (image URL): ")
    alt_text = input("Enter Alt Text: ")

    if not validate_required_fields({"Picture": image_content}):
        return

    image_id = get_next_image_id(textbook_id, chapter_id, section_id, block_id)

    while True:
        print("\nMenu:")
        print("1. Add")
        print("2. Go Back")
        print("3. Landing Page")
        choice = input("Enter choice (1-3): ")

        match choice:
            case '1':
                if insert_image_content(textbook_id, chapter_id, section_id, block_id, image_id, image_content, alt_text):
                    print("Picture added successfully.")
                    return
                else:
                    print("Failed to add picture. Please try again.")
            case '2':
                return
            case '3':
                print("Returning to User Landing Page...")
                reset = True
                return
            case _:
                print("Invalid choice. Please enter 1, 2, or 3.")

def add_activity_page(user_id, textbook_id, chapter_id, section_id, block_id):
    global reset
    print("\nAdmin: Add Activity")
    activity_id = input("Enter the unique Activity ID: ")

    if not validate_required_fields({"Activity ID": activity_id}):
        return
    
    if insert_activity(textbook_id, chapter_id, section_id, block_id, activity_id, user_id):
        print("Activity added successfully.")
    else:
        return

    while True:
        print("\nMenu:")
        print("1. Add Question")
        print("2. Go Back")
        print("3. Landing Page")
        choice = input("Enter choice (1-3): ")

        match choice:
            case '1':
                add_question_page(user_id, textbook_id, chapter_id, section_id, block_id, activity_id)
                if(reset == True):
                    return
            case '2':
                return
            case '3':
                print("Returning to User Landing Page...")
                reset = True
                return
            case _:
                print("Invalid choice. Please enter 1, 2, or 3.")

def add_question_page(user_id, textbook_id, chapter_id, section_id, block_id, activity_id):
    global reset
    print("\nAdmin: Add Question")
    question_id = input("Enter Question ID: ")
    question_text = input("Enter Question Text: ")

    options = []
    correct_count = 0

    for i in range(1, 5):
        option_text = input(f"Enter Option {i} Text: ")
        option_explanation = input(f"Enter Option {i} Explanation: ")
        correct = input(f"Is Option {i} Correct? (yes/no): ").strip().lower() == 'yes'
        options.append((option_text, option_explanation, correct))

        if correct:
            correct_count += 1

    if correct_count != 1:
        print("Error: There must be exactly one correct answer. Please try again.")
        return

    if not validate_required_fields({
        "Question ID": question_id,
        "Question Text": question_text,
        **{f"Option {i}": option[0] for i, option in enumerate(options, start=1)},
        **{f"Option {i} Explanation": option[1] for i, option in enumerate(options, start=1)}
    }):
        return

    correct_answer = next((i + 1 for i, opt in enumerate(options) if opt[2]), None)

    if insert_question(textbook_id, chapter_id, section_id, block_id, activity_id, question_id, question_text, options, correct_answer, user_id):
        print("Question added successfully.")
    else:
        print("Failed to add question. Please try again.")


def create_active_course_page(user_id):
    global reset
    print("\nAdmin: Create New Active Course")

    faculty_list = get_faculty_list()
    textbook_list = get_textbook_list()
    
    course_id = input("\nEnter Unique Course ID: ")
    course_name = input("Enter Course Name: ")
    print("\nList of Available Textbooks:")
    for textbook in textbook_list:
        print(f"ID: {textbook[0]}, Title: {textbook[1]}")
        
    while True:
        textbook_id = validate_integer_input("Enter Unique ID of the E-textbook: ")
        if validate_textbook_id(textbook_id, textbook_list):
            break
        else:
            print("Invalid Textbook ID. Please enter a valid ID from the list above.")
            
    print("\nList of Faculty Members:")
    for faculty in faculty_list:
        print(f"ID: {faculty[0]}, Name: {faculty[1]} {faculty[2]}, Email: {faculty[3]}")
    while True:
        faculty_id = input("Enter Faculty Member ID: ")
        if validate_faculty_id(faculty_id, faculty_list):
            break
        else:
            print("Invalid Faculty ID. Please enter a valid ID from the list above.")

    start_date = input("Enter Course Start Date (YYYY-MM-DD): ")
    end_date = input("Enter Course End Date (YYYY-MM-DD): ")
    unique_token = input("Enter Unique Token (6 characters): ")
    capacity = validate_integer_input("Enter Course Capacity: ")

    while True:
        print("\nMenu:")
        print("1. Save")
        print("2. Cancel")
        print("3. Landing Page")
        choice = input("Enter choice (1-3): ")

        match choice:
            case '1':
                if insert_active_course(course_id, course_name, textbook_id, faculty_id, start_date, end_date, unique_token, capacity, user_id):
                    print("New active course created successfully.")
                    return
                else:
                    print("Failed to create active course. Please try again.")
                    return
            case '2':
                print("Cancelling and returning to previous page...")
                return
            case '3':
                print("Returning to User Landing Page...")
                reset = True
                return
            case _:
                print("Invalid choice. Please enter 1, 2, or 3.")