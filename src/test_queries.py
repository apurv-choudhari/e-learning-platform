from mysql.connector import Error
from flow.admin.admin_db_utils import connectDB

def execute_query(query_num):
    conn, cursor = connectDB()
    if conn is None or cursor is None:
        print("Database connection failed.")
        return

    # TODO:
    # Write queries here
    queries = {
        1: "SELECT * FROM user;",
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
            cursor.execute(query)
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

def test_user_queries():
    while True:
        print("\n--- Query Executor ---")
        print("1. Execute Query 1")
        print("2. Execute Query 2")
        print("3. Execute Query 3")
        print("4. Execute Query 4")
        print("5. Execute Query 5")
        print("6. Execute Query 6")
        print("7. Execute Query 7")
        print("8. Back to Main Menu")

        choice = input("Enter your choice (1-8): ")

        if choice in [str(i) for i in range(1, 8)]:
            execute_query(int(choice))
        elif choice == "8":
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    test_user_queries()
