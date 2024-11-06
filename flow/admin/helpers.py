def validate_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

def validate_required_fields(fields):
    for field_name, value in fields.items():
        if value == "":
            print(f"Error: {field_name} is required and cannot be empty.")
            return False
    return True

def validate_faculty_id(faculty_id, faculty_list):
    valid_ids = [faculty[0] for faculty in faculty_list]
    return faculty_id in valid_ids

def validate_textbook_id(textbook_id, textbook_list):
    valid_ids = [textbook[0] for textbook in textbook_list]
    return textbook_id in valid_ids

def validate_chapter_id(chapter_id, chapter_list):
    valid_ids = [chapter[0] for chapter in chapter_list]
    return chapter_id in valid_ids

def validate_section_id(section_id, section_list):
    valid_ids = [section[0] for section in section_list]
    return section_id in valid_ids

def validate_block_id(block_id, content_block_list):
    valid_ids = [block[0] for block in content_block_list]
    return block_id in valid_ids

def validate_question_id(question_id, question_list):
    valid_ids = [question[0] for question in question_list]
    return question_id in valid_ids
