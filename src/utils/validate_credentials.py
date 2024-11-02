from db_utils import connectDB

def validate_credentials(user_id, password, role):
    """
    Validates user credentials for a given role.
    Parameters:
    - user_id: str, the user ID.
    - password: str, the password.
    - role: int, the role number (1 for Admin, 2 for Faculty, etc.).

    Returns:
    - bool: True if credentials are valid, False otherwise.
    """
    _, cursor = connectDB()
    try:
        query = "SELECT password FROM user WHERE user_id = %s AND role_no = %s"
        cursor.execute(query, (user_id, role))
        result = cursor.fetchone()
        return result and result[0] == password
    finally:
        cursor.close()

def login_flow(role):
    while True:
        user_id = input("User ID: ")
        password = input("Password: ")
        print('1. Sign-in')
        print('2. Go Back')
        action_choice = input('Enter Choice (1-2): ')

        if action_choice == '1':
            if validate_credentials(user_id, password, role):
                print(f"Login Successful. Welcome, {user_id}!")
                return user_id, True
            else:
                print("Incorrect credentials. Enter Again")                
        else:
            return '', False
