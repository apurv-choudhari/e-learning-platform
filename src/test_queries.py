from mysql.connector import Error
from flow.admin.admin_db_utils import connectDB

def execute_query(query_num, param_list):
    conn, cursor = connectDB()
    if conn is None or cursor is None:
        print("Database connection failed.")
        return

    # TODO:
    # Write queries here
    queries = {
        1: "select count(section_id) from section where chapter_id = 'chap01' and textbook_id = %s;",
        2: "SELECT * FROM textbook;",
        3: "SELECT * FROM course;",
        4: "SELECT * FROM faculty;",
        5: "SELECT * FROM section;",
        6: "SELECT * FROM content_block;",
        7: "SELECT * FROM activity;"
    }

    try:
        query = queries.get(query_num)
        if query:
            cursor.execute(query, param_list)
            if query_num in {1, 2, 3, 4, 5, 6, 7}:
                results = cursor.fetchall()
                for row in results:
                    print(row)
            else:
                print("Invalid query number.")

    except Error as e:
        print(f"An error occurred while executing query {query_num}: {e}")

    finally:
        cursor.close()
        conn.close()


def params_for_query_1():
    tid = input("Provide Textbook-id: ")
    return [tid]

def no_params():
    return []

get_query_params = {
    "1": params_for_query_1,
    # "2": params_for_query_2,
    # "3": params_for_query_3,
    # "4": params_for_query_4
}

def test_user_queries():
    while True:
        print("\n--- Query Executor ---")
        print("1. Query 1: Write a query that prints the number of sections of the first chapter of a textbook.")
        print("2. Execute Query 2")
        print("3. Execute Query 3")
        print("4. Execute Query 4")
        print("5. Execute Query 5")
        print("6. Execute Query 6")
        print("7. Execute Query 7")
        print("8. Back to Main Menu")

        choice = input("Enter your choice (1-8): ")

        if choice in [str(i) for i in range(1, 8)]:
            param_list = get_query_params[choice]()
            execute_query(int(choice), param_list)
        elif choice == "8":
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    test_user_queries()
