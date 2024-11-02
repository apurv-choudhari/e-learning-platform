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

def execute_query(query_num):
    # TODO: Implement the cursor logic here
    # Simulating query execution
    result = f"Executing Query {query_num}..."
    print(result)

# Test function
if __name__ == "__main__":
    test_user_queries()
