from flow.admin.admin_db_utils import insert_textbook, insert_chapter, insert_section, insert_content_block, insert_text_content, insert_image_content, insert_user, insert_activity, insert_question, get_next_text_id, get_next_image_id
from flow.admin.helpers import validate_integer_input, validate_required_fields

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
                create_textbook_page(user_id)
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
            case '2':
                print("Returning to Admin Landing Page...")
                return
            case _:
                print("Invalid choice. Please enter 1 or 2.")

def create_chapter_page(user_id, textbook_id):
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
                case '2':
                    print("Returning to previous page...")
                    return False
                case '3':
                    print("Returning to User Landing Page...")
                    return False
                case _:
                    print("Invalid choice. Please enter 1, 2, or 3.")
    else:
        print("Failed to create chapter. Please check the details and try again.")
        return False

def create_section_page(user_id, textbook_id, chapter_id):
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
                case '2':
                    print("Returning to previous page...")
                    return
                case '3':
                    print("Returning to User Landing Page...")
                    return
                case _:
                    print("Invalid choice. Please enter 1, 2, or 3.")
    else:
        print("Failed to add section. Please check the details and try again.")

def create_content_block_page(user_id, textbook_id, chapter_id, section_id):
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
        else:
            print("Failed to add content block.")
    elif choice == '2':
        content_type = "image"
        if insert_content_block(textbook_id, chapter_id, section_id, block_id, content_type, user_id):
            add_image_page(user_id, textbook_id, chapter_id, section_id, block_id)
        else:
            print("Failed to add content block.")
    elif choice == '3':
        content_type = "activity"
        if insert_content_block(textbook_id, chapter_id, section_id, block_id, content_type, user_id):
            add_activity_page(user_id, textbook_id, chapter_id, section_id, block_id)
        else:
            print("Failed to add content block.")
    elif choice == '4':
        print("Going back to the previous page...")
        return
    elif choice == '5':
        print("Returning to User Landing Page...")
        return
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
        return

def add_text_page(user_id, textbook_id, chapter_id, section_id, block_id):
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
                return
            case _:
                print("Invalid choice. Please enter 1, 2, or 3.")


def add_image_page(user_id, textbook_id, chapter_id, section_id, block_id):
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
                return
            case _:
                print("Invalid choice. Please enter 1, 2, or 3.")

def add_activity_page(user_id, textbook_id, chapter_id, section_id, block_id):
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
            case '2':
                return
            case '3':
                print("Returning to User Landing Page...")
                return
            case _:
                print("Invalid choice. Please enter 1, 2, or 3.")

def add_question_page(user_id, textbook_id, chapter_id, section_id, block_id, activity_id):
    print("\nAdmin: Add Question")
    question_id = input("Enter Question ID: ")
    question_text = input("Enter Question Text: ")

    options = []
    for i in range(1, 5):
        option_text = input(f"Enter Option {i} Text: ")
        option_explanation = input(f"Enter Option {i} Explanation: ")
        correct = input(f"Is Option {i} Correct? (yes/no): ").strip().lower() == 'yes'
        options.append((option_text, option_explanation, correct))

    if not validate_required_fields({
        "Question ID": question_id,
        "Question Text": question_text,
        **{f"Option {i}": option[0] for i, option in enumerate(options, start=1)},
        **{f"Option {i} Explanation": option[1] for i, option in enumerate(options, start=1)}
    }):
        return

    correct_answer = next((i + 1 for i, opt in enumerate(options) if opt[2]), None)

    if correct_answer is None:
        print("Error: At least one option must be marked as correct.")
        return

    if insert_question(textbook_id, chapter_id, section_id, block_id, activity_id, question_id, question_text, options, correct_answer, user_id):
        print("Question added successfully.")
    else:
        print("Failed to add question. Please try again.")
