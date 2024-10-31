import tkinter as tk
from tkinter import messagebox
from main import connectDB
from ui_test_queries import open_queries_window
import subprocess

_, cursor = connectDB()

def login():
    user_types = {
        "Admin": 1,
        "Faculty": 2,
        "Student": 3,
        "TA": 4
    }
    username = username_entry.get()
    password = password_entry.get()
    user_type = user_types[user_type_var.get()]

    if username and password and user_type:
        command = f"SELECT password FROM user WHERE user_id = '{username}' AND role_no = '{user_type}'"
        print(command)
        cursor.execute(command)
        result = cursor.fetchall()
        print(f"Query Result: {result}")

        if not result:
            messagebox.showinfo("Fail", "Data Not Found. Please check if the username, password and the role is correct.")
            return

        db_password = result[0][0]

        if db_password == password:
            print("Login Success")
            messagebox.showinfo("Success", f"Login Success.\nUsername: {username}\nPassword: {password}\nUser Type: {user_type}")
        else:
            messagebox.showinfo("Fail", "Login Failed.")
    else:
        messagebox.showwarning("Incomplete Data", "Please fill in all fields.")

root = tk.Tk()
root.title("User Information")
root.geometry("300x250")

username_label = tk.Label(root, text="Username:")
username_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=10)

password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)

user_type_label = tk.Label(root, text="User Type:")
user_type_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
user_type_var = tk.StringVar(root)
user_type_var.set("Admin")
user_type_dropdown = tk.OptionMenu(root, user_type_var, "Admin", "Faculty", "Student", "TA")
user_type_dropdown.grid(row=2, column=1, padx=10, pady=10)

submit_button = tk.Button(root, text="Login", command=login)
submit_button.grid(row=3, column=0, padx=(20, 5), pady=10, sticky="w")

exit_button = tk.Button(root, text="Exit", command=root.quit)
exit_button.grid(row=3, column=1, padx=(5, 20), pady=10, sticky="e")

queries_button = tk.Button(root, text="Queries", command=lambda:open_queries_window(root))
queries_button.grid(row=4, column=0, columnspan=2, pady=20)

root.mainloop()
