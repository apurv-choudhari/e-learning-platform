from utils.validate_credentials import login_flow
from flow.faculty.faculty_db_utils import get_textbook_id, select_courses, update_password, select_waitlist, update_enrollment_status, select_students, insert_ta, insert_chapter, hide_chapter_util, del_chapter
from flow.faculty.faculty_db_utils import insert_section, hide_section_util, del_section, insert_content_block, insert_text, insert_image, insert_activity, insert_question
from flow.faculty.faculty_db_utils import hide_content_block_util, del_content_block, hide_activity_util, del_activity, validate_active_course, validate_enrollment_course
from flow.admin.helpers import validate_integer_input, validate_required_fields
from flow.admin.admin_db_utils import get_next_text_id, get_next_image_id

def faculty_flow(user_id):
    print("Faculty Landing Page. Welcome, " + user_id + "!")
    while True:
        print("\nFaculty Menu:")
        print("1. Go to Active Course")
        print("2. Go to Evaluation Course")
        print("3. View Courses")
        print("4. Change Password")
        print("5. Logout")
        
        choice = input("Enter choice (1-5): ")

        match choice:
            case '1':
                print("\nRedirecting to Active Courses...")
                active_course(user_id)
            case '2':
                print("\nRedirecting to Evaluation Courses...")
                evaluation_course(user_id)
            case '3':
                print("\nRedirecting to Courses...")
                view_courses(user_id)
            case '4':
                print("\nRedirecting to Change Password")
                change_password(user_id)
            case '5':
                print("\nLogging out...")
                break
            case _:
                print("\nInvalid choice. Please enter a number between 1 and 5.")

def active_course(user_id):
    print("\nActive Course Page")
    course_id =  input("Provide Course ID: ")
    is_active = validate_active_course(course_id)
    if not is_active:
        print("The course id does not belong to an active course")
        return
    while True:
        print(f"You are viewing Active Course - {course_id}")
        print("\n Menu")
        print("1. View Waitlist")
        print("2. Approve Enrollment")
        print("3. View Students")
        print("4. Add New Chapters")
        print("5. Modify Chapters")
        print("6. Add TA")
        print("7. Go Back")

        choice = input("Enter choice (1-7): ")

        match choice:
            case '1':
                print("\nRedirecting to Waitlist...")
                view_waitlist(course_id)
            case '2':
                print("\nRedirecting to Approve Enrollment")
                approve_enrollment(course_id)
            case '3':
                print("\nRedirecting to View Students")
                view_students(course_id)
            case '4':
                print("\nRedirecting to Add New Chapters")
                add_chapter(user_id, course_id)
            case '5':
                print("\nRedirecting to Modify Chapters")
                modify_chapter(user_id, course_id)
            case '6':
                print("\nRedirecting to Add TA")
                add_ta(user_id, course_id)
            case '7':
                return
            case _:
                print("Invalid choice. Please enter 1 to 7")
    return

def evaluation_course(user_id):
    print("\n Evaluation Course Page")
    course_id =  input("Provide Course ID: ")
    is_enrollment = validate_enrollment_course(course_id)
    if not is_enrollment:
        print("The course id does not belong to an enrollment course")
        return
    while True:
        print(f"You are viewing Active Course - {course_id}")
        print("\n Menu")
        print("1. Add New Chapters")
        print("2. Modify Chapters")
        print("3. Go Back")

        choice = input("Enter choice (1-3): ")
        
        match choice:
                case '1':
                    print("\nRedirecting to Add New Chapter")
                    add_chapter(user_id, course_id)
                case '2':
                    print("\nRedirecting to Modify Chapters")
                    modify_chapter(user_id, course_id)
                case '3':
                    return
                case _:
                    print("Invalid choice. Please enter 1-3")
    return

def view_courses(user_id):
    while True:
        print("View Courses Page")
        courses = select_courses(user_id)
        # Print each course
        if courses:
            print("Courses for faculty_id", user_id, ":")
            for course in courses:
                print(course)
        else:
            print("No courses found for faculty_id", user_id)
        
        print("\n Menu")
        print("1. Go Back")

        choice = input("Enter choice (1): ")
        
        match choice:
                case '1':
                    print("\nRedirecting to Previous page")
                    return
    return

def change_password(user_id):
    print("Change Password")
    current_password = input("Enter Current Password: ")
    new_password = input("Enter New Password: ")
    confirm_new_password = input("Confirm New Password: ")

    while True:
        print("\n Menu")
        print("1. Update ")
        print("2. Go Back")
        
        choice = input("Enter choice (1-2): ")
        
        match choice:
                case '1':
                    print("\nChanging Password... ")
                    update_password(user_id, current_password , new_password, confirm_new_password)
                    return
                case '2':
                    print("\nRedirecting to Previous page")
                    return
                case _:
                    print("Invalid choice. Please enter 1 or 2")
    return

def view_waitlist(course_id):
    while True:
        print("View Waiting List of Students")
        select_waitlist(course_id)
        print("\n Menu")
        print("1. Go Back")

        choice = input("Enter choice (1): ")
        
        match choice:
                case '1':
                    print("\nRedirecting to Previous page")
                    return
    return

def approve_enrollment(course_id):
    while True:
        print("Approve Student Enrollment")
        student_id =  input("Provide Student ID to approve enrollment: ")
        print("\n Menu")
        print("1. Save")
        print("2. Cancel")

        choice = input("Enter choice (1): ")
        
        match choice:
                case '1':
                    print("Saving in database...")
                    update_enrollment_status(course_id, student_id)
                case '2':
                    print("\nRedirecting to Previous page")
                    return
                case _:
                    print("Invalid choice. Please enter 1 or 2")
    return

def view_students(course_id):
    print("View Students Page")
    while True:
        select_students(course_id)
        print("\n Menu")
        print("1. Go Back")

        choice = input("Enter choice (1): ")
        
        match choice:
                case '1':
                    print("\nRedirecting to Previous page")
                    return
    return

def add_ta(fac_user_id, course_id):
    print("\nAdd a Teaching Assistant (TA)")
    user_id = input("Enter Username: ")
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    email = input("Enter Email: ")

    if not validate_required_fields({
        "Username": user_id,
        "First Name": first_name,
        "Last Name": last_name,
        "Email": email,
    }):
        return
    
    while True:
        print("\n Menu")
        print("1. Save")
        print("2. Cancel")

        choice = input("Enter choice (1): ")
        
        match choice:
                case '1':
                    print("Adding to database...")
                    insert_ta(user_id, first_name, last_name, email, fac_user_id, course_id)
                case '2':
                    print("\nRedirecting to Previous page")
                    return
                case _:
                    print("Invalid choice. Please enter 1 or 2")
    return

def add_chapter(user_id, course_id):
    print("\nFaculty: Add New Chapter")
    chapter_id = input("Enter the unique Chapter ID: ")
    chapter_title = input("Enter the Chapter Title: ")

    if not validate_required_fields({
        "Chapter ID": chapter_id,
        "Chapter Title": chapter_title
    }):
        return
    
    if insert_chapter(user_id, course_id, chapter_id, chapter_title):
        while True:
            print(f"You are viewing Chapter - {chapter_id}")
            print("\nMenu:")
            print("1. Add New Section")
            print("2. Go Back")
            choice = input("Enter choice (1-2): ")

            match choice:
                case '1':
                    print("Redirecting to Add New Section page...")
                    add_new_section(user_id, course_id, chapter_id)
                case '2':
                    print("Returning to previous page...")
                    return False
                case _:
                    print("Invalid choice. Please enter 1 or 2")
    else:
        print("Failed to create chapter. Please check the details and try again.")
        return False
    
def modify_chapter(user_id, course_id):
    print("\nFaculty: Modify Chapter")
    chapter_id = input("Enter the unique Chapter ID: ")
    while True:
        print(f"You are viewing Chapter - {chapter_id}")
        print("\nMenu")
        print("1. Hide Chapter")
        print("2. Delete Chapter")
        print("3. Add New Section")
        print("4. Modify Section")
        print("5. Go Back")
        choice = input("Enter choice (1-5): ")

        match choice:
            case '1':
                print("\nRedirecting to Hide Chapter...")
                hide_chapter(user_id, course_id, chapter_id)
            case '2':
                print("\nRedirecting to Delete Chapter...")
                delete_chapter(user_id, course_id, chapter_id)
            case '3':
                print("\nRedirecting to Add New Section...")
                add_new_section(user_id, course_id, chapter_id)
            case '4':
                print("\nRedirecting to Modify Section...")
                modify_section(user_id, course_id, chapter_id)
            case '5':
                print("\nRedirecting to previous page...")
                return
            case _:
                print("Invalid choice. Please enter 1-5")
    return
            
def hide_chapter(user_id, course_id, chapter_id):
    print("Faculty: Hide Chapter")
    while True:
        print("\n Menu")
        print("1. Save")
        print("2. Cancel")

        choice = input("Enter choice (1-2): ")
        
        match choice:
                case '1':
                    print("Saving changes in database...")
                    hide_chapter_util(user_id, course_id, chapter_id)
                case '2':
                    print("\nRedirecting to Previous page")
                    return
                case _:
                    print("Invalid choice. Please enter 1 or 2")
    return

def delete_chapter(user_id, course_id, chapter_id):
    print("Faculty: Delete Chapter")
    while True:
        print("\n Menu")
        print("1. Save")
        print("2. Cancel")

        choice = input("Enter choice (1-2): ")
        
        match choice:
                case '1':
                    print("Saving in database...")
                    res = del_chapter(user_id, course_id, chapter_id)
                    if not res:
                        return
                case '2':
                    print("\nRedirecting to Previous page")
                    return
                case _:
                    print("Invalid choice. Please enter 1 or 2")
    return

def add_new_section(user_id, course_id, chapter_id):
    print("\nFaculty: Add New Section")
    section_id = input("Enter the unique Section ID: ")
    section_title = input("Enter the Section Title: ")

    if insert_section(course_id, chapter_id, section_id, section_title, user_id):
        while True:
            print(f"You are viewing Section - {section_id}")
            print("\nMenu:")
            print("1. Add New Content Block")
            print("2. Go Back")
            choice = input("Enter choice (1-2): ")

            match choice:
                case '1':
                    print("Redirecting to Add New Content Block")
                    add_content_block(user_id, course_id, chapter_id, section_id)
                case '2':
                    print("Returning to previous page...")
                    return
                case _:
                    print("Invalid choice. Please enter 1 or 2")
    else:
        print("Failed to add section. Please check the details and try again.")
        return

def modify_section(user_id, course_id, chapter_id):
    print("\nFaculty: Modify Section")
    section_id = input("Enter the Section no:")
    while True:
        print(f"You are viewing Section - {section_id}")
        print("1. Hide Section")
        print("2. Delete Section")
        print("3. Add New Content Block")
        print("4. Modify Content Block")
        print("5. Go Back")
        choice = input("Enter choice (1-5): ")

        match choice:
            case '1':
                print("\nRedirecting to Hide Section...")
                hide_section(user_id, course_id, chapter_id, section_id)
            case '2':
                print("\nRedirecting to Delete Section...")
                delete_section(user_id, course_id, chapter_id, section_id)
            case '3':
                print("\nRedirecting to Add New Content Block...")
                add_content_block(user_id, course_id, chapter_id, section_id)
            case '4':
                print("\nRedirecting to Modify Content Block...")
                modify_content_block(user_id, course_id, chapter_id, section_id)
            case '5':
                print("\nRedirecting to previous page...")
                return
            case _:
                print("Invalid choice. Please enter 1 - 5")
    return

def hide_section(user_id, course_id, chapter_id, section_id):
    while True:
        print("Faculty: Hide Section")
        print("\n Menu")
        print("1. Save")
        print("2. Cancel")

        choice = input("Enter choice (1-2): ")
        
        match choice:
                case '1':
                    print("Saving in database...")
                    hide_section_util(user_id, course_id, chapter_id, section_id)
                case '2':
                    print("\nRedirecting to Previous page")
                    return
    return

def delete_section(user_id, course_id, chapter_id, section_id):
    while True:
        print("Faculty: Delete Section")
        print("\n Menu")
        print("1. Save")
        print("2. Cancel")

        choice = input("Enter choice (1-2): ")
        
        match choice:
                case '1':
                    print("Saving changes in database...")
                    del_section(user_id, course_id, chapter_id, section_id)
                case '2':
                    print("\nRedirecting to Previous page")
                    return
                case _:
                    print("Invalid choice. Please enter 1 or 2")
    return

def add_content_block(user_id, course_id, chapter_id, section_id):
    print("\nFaculty: Add New Content Block")
    block_id = input("Enter the unique Content Block ID: ")
    while True:
        print(f"You are viewing Block - {block_id}")
        print("\nMenu:")
        print("1. Add Text")
        print("2. Add Picture")
        print("3. Add Activity")
        print("4. Go Back")
        choice = input("Enter choice (1-4): ")

        match choice:
            case '1':
                content_type = 'text'
                if insert_content_block(user_id, course_id, chapter_id, section_id, block_id, content_type):
                    print("\nRedirecting to Add Text...")
                    add_text(user_id, course_id, chapter_id, section_id, block_id)
                else: return
                    
            case '2':
                content_type = 'image'
                if insert_content_block(user_id, course_id, chapter_id, section_id, block_id, content_type):
                    print("\nRedirecting to Add Picture...")
                    add_picture(user_id, course_id, chapter_id, section_id, block_id)
                else: return
            case '3':
                content_type = 'activity'
                if insert_content_block(user_id, course_id, chapter_id, section_id, block_id, content_type):
                    print("\nRedirecting to Add Activity...")
                    add_activity(user_id, course_id, chapter_id, section_id, block_id)
                else: return
            case '4':
                print("\nRedirecting to Previous page...")
                return
            case _:
                print("Invalid choice. Please enter 1 - 4")
    return

def modify_content_block(user_id, course_id, chapter_id, section_id):
    print("\nFaculty: Modify Content Block")
    block_id = input("Enter the Content Block id:")
    while True:
        print(f"You are viewing Block - {block_id}")
        print("\nMenu:")
        print("1. Hide Content Block")
        print("2. Delete Content Block")
        print("3. Add Text")
        print("4. Add Picture")
        print("5. Hide Activity")
        print("6. Delete Activity")
        print("7. Add Activity")
        print("8. Go Back")
        choice = input("Enter choice (1-8): ")

        match choice:
            case '1':
                print("\nRedirecting to Hide Content Block...")
                hide_content_block(user_id, course_id, chapter_id, section_id, block_id)
            case '2':
                print("\nRedirecting to Delete Content Block...")
                delete_content_block(user_id, course_id, chapter_id, section_id, block_id)
            case '3':
                print("\nRedirecting to Add Text...")
                add_text(user_id, course_id, chapter_id, section_id, block_id)
            case '4':
                print("\nRedirecting to Add Picture...")
                add_picture(user_id, course_id, chapter_id, section_id, block_id)
            case '5':
                print("\nRedirecting to Hide Activity...")
                hide_activity(user_id, course_id, chapter_id, section_id, block_id)
            case '6':
                print("\nRedirecting to Delete Activity...")
                delete_activity(user_id, course_id, chapter_id, section_id, block_id)
            case '7':
                print("\nRedirecting to Add Activity...")
                add_activity(user_id, course_id, chapter_id, section_id, block_id)    
            case '8':
                print("\nRedirecting to previous page...")
                return
            case _:
                print("Invalid choice. Please enter 1 to 8")

def hide_content_block(user_id, course_id, chapter_id, section_id, block_id):
    print("Faculty: Hide Content Block")
    while True:
        print("\n Menu")
        print("1. Save")
        print("2. Cancel")

        choice = input("Enter choice (1-2): ")
        
        match choice:
                case '1':
                    print("Saving in database...")
                    hide_content_block_util(user_id, course_id, chapter_id, section_id, block_id)
                case '2':
                    print("\nRedirecting to Previous page")
                    return
                case _:
                    print("Invalid choice. Please enter 1 or 2")

def delete_content_block(user_id, course_id, chapter_id, section_id, block_id):
    print("Faculty: Delete Content Block")
    while True:
        print("\n Menu")
        print("1. Save")
        print("2. Cancel")

        choice = input("Enter choice (1-2): ")
        
        match choice:
                case '1':
                    print("Saving in database...")
                    del_content_block(user_id, course_id, chapter_id, section_id, block_id)
                case '2':
                    print("\nRedirecting to Previous page")
                    return
                case _:
                    print("Invalid choice. Please enter 1 or 2")

def add_text(user_id, course_id, chapter_id, section_id, block_id):
    print("\nFaculty: Add Text")
    text_content = input("Enter the text to be added: ")
    if not validate_required_fields({"Text": text_content}):
        return
    textbook_id = get_textbook_id(course_id, user_id)
    text_id = get_next_text_id(textbook_id, chapter_id, section_id, block_id)
    while True:
        print("\nMenu:")
        print("1. Add")
        print("2. Go Back")
        choice = input("Enter choice (1-2): ")

        match choice:
            case '1':
                if insert_text(textbook_id, chapter_id, section_id, block_id, text_id, text_content):
                    print("Text added successfully.")
                    return
                else:
                    print("Failed to add text. Please try again.")
                    return
            case '2':
                return
            case _:
                print("Invalid choice. Please enter 1 or 2.")

    return

def add_picture(user_id, course_id, chapter_id, section_id, block_id):
    print("\nFaculty: Add Picture")
    image_content = input("Enter the Picture (image URL): ")
    alt_text = input("Enter Alt Text: ")

    if not validate_required_fields({"Picture": image_content}):
        return
    
    textbook_id = get_textbook_id(course_id, user_id)
    image_id = get_next_image_id(textbook_id, chapter_id, section_id, block_id)

    while True:
        print("\nMenu:")
        print("1. Add")
        print("2. Go Back")
        choice = input("Enter choice (1-2): ")

        match choice:
            case '1':
                if insert_image(textbook_id, chapter_id, section_id, block_id, image_id, image_content, alt_text):
                    print("Picture added successfully.")
                    return
                else:
                    print("Failed to add picture. Please try again.")
            case '2':
                return
            case _:
                print("Invalid choice. Please enter 1 or 2")
    return

def hide_activity(user_id, course_id, chapter_id, section_id, block_id):
    print("Faculty: Hide Activity")
    activity_id = input("Enter the unique Activity ID: ")
    while True:
        print("\n Menu")
        print("1. Save")
        print("2. Cancel")

        choice = input("Enter choice (1-2): ")
        
        match choice:
                case '1':
                    print("Saving chages in database...")
                    hide_activity_util(user_id, course_id, chapter_id, section_id, block_id, activity_id)
                case '2':
                    print("\nRedirecting to Previous page")
                    return
                case _:
                    print("Invalid choice. Please enter 1 or 2")
    return

def delete_activity(user_id, course_id, chapter_id, section_id, block_id):
    print("Faculty: Delete Activity")
    activity_id = input("Enter the unique Activity ID: ")
    while True:
        print("\n Menu")
        print("1. Save")
        print("2. Cancel")

        choice = input("Enter choice (1-2): ")
        
        match choice:
                case '1':
                    print("Saving changes in database...")
                    del_activity(user_id, course_id, chapter_id, section_id, block_id, activity_id)
                case '2':
                    print("\nRedirecting to Previous page")
                    return
                case _:
                    print("Invalid choice. Please enter 1 or 2")
    return

def add_activity(user_id, course_id, chapter_id, section_id, block_id):
    print("\nFaculty: Add Activity")
    activity_id = input("Enter the unique Activity ID: ")
    
    if not validate_required_fields({"Activity ID": activity_id}):
        return
    textbook_id = get_textbook_id(course_id, user_id)

    if insert_activity(textbook_id, chapter_id, section_id, block_id, activity_id, user_id):
        while True:
            print("\nMenu:")
            print(f"You are viewing Activity - {activity_id}")
            print("1. Add Question")
            print("2. Go Back")
            choice = input("Enter choice (1-2): ")

            match choice:
                case '1':
                    add_question(user_id, course_id, chapter_id, section_id, block_id, activity_id)
                case '2':
                    return
                case _:
                    print("Invalid choice. Please enter 1 or 2")
    else:
        print("Failed to create activity. Please check the details and try again.")

def add_question(user_id, course_id, chapter_id, section_id, block_id, activity_id):
    print("\nFaculty: Add Question")
    question_id = input("Enter Question ID: ")
    question_text = input("Enter Question Text: ")
    options = []
    for i in range(1, 5):
        option_text = input(f"Enter Option {i} Text: ")
        option_explanation = input(f"Enter Option {i} Explanation: ")
        options.append((option_text, option_explanation))
    
    if not validate_required_fields({
        "Question ID": question_id,
        "Question Text": question_text,
        **{f"Option {i}": option[0] for i, option in enumerate(options, start=1)},
        **{f"Option {i} Explanation": option[1] for i, option in enumerate(options, start=1)}
    }):
        return
    
    correct_answer = int(input(f"Enter the correct option ? (1/2/3/4): "))

    if correct_answer is None:
        print("Error: At least one option must be marked as correct.")
        return
    
    textbook_id = get_textbook_id(course_id, user_id)
    while True:
        print("\nMenu:")
        print("1. Save")
        print("2. Cancel")
        choice = input("Enter choice (1-2): ")

        match choice:
            case '1':
                if insert_question(textbook_id, chapter_id, section_id, block_id, activity_id, question_id, question_text, options, correct_answer, user_id):
                    print("Question added successfully.")
                else:
                    print("Failed to add question. Please try again.")
            case '2':
                return
            case _:
                print("Invalid choice. Please enter 1 or 2")
    
    
