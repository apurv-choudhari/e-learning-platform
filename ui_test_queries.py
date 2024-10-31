import tkinter as tk
from tkinter import messagebox

def open_queries_window(root):
    root.withdraw()
    queries_window = tk.Toplevel(root)
    queries_window.title("Query Executor")
    queries_window.geometry("500x400")
    
    back_button = tk.Button(queries_window, text="Back", command=lambda: back_to_login(queries_window, root))
    back_button.pack(pady=10)

    for i in range(1, 8):
        button = tk.Button(queries_window, text=f"Execute Query {i}", command=lambda i=i: execute_query(i))
        button.pack(pady=5)

def back_to_login(queries_window, root):
    queries_window.destroy()
    root.deiconify()

def execute_query(query_num):
    # TODO
    # The cursor logic goes here
    result = f"Executing Query {query_num}..."
    messagebox.showinfo("Query Execution", result)
