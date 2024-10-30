import tkinter as tk
from tkinter import scrolledtext

# Placeholder functions for the queries (replace with actual queries)
def query1():
    return "Output of Query 1: [Result Data 1]"

def query2():
    return "Output of Query 2: [Result Data 2]"

def query3():
    return "Output of Query 3: [Result Data 3]"

def query4():
    return "Output of Query 4: [Result Data 4]"

def query5():
    return "Output of Query 5: [Result Data 5]"

def query6():
    return "Output of Query 6: [Result Data 6]"

def query7():
    return "Output of Query 7: [Result Data 7]"

def execute_query(query_num):
    result = globals()[f"query{query_num}"]()
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, result)

def connect_to_db():
    return "Connected to the database."

def create_app():
    root = tk.Tk()
    root.title("Query Executor")

    root.state('zoomed')

    buttons = []
    for i in range(1, 8):
        button = tk.Button(root, text=f"Execute Query {i}", command=lambda i=i: execute_query(i), height=2, width=20)
        button.pack(pady=10)
        buttons.append(button)

    global output_text
    output_text = scrolledtext.ScrolledText(root, width=100, height=30, wrap=tk.WORD)
    output_text.pack(pady=10)

    # Start the application
    root.mainloop()

db_connection = connect_to_db()
print(db_connection)

create_app()
