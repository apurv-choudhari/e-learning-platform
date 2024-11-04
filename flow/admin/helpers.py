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
