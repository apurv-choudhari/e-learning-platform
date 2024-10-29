import tkinter as tk
from tkinter import messagebox

try:
    def login():
        user_types = {
            "Admin" : 1,
            "Teacher" : 2,
            "TA" : 3,
            "Student": 4
        }
        username = username_entry.get()
        password = password_entry.get()
        user_type = user_types[user_type_var.get()]

        if username and password and user_type:
            #Invoke user based login here
            messagebox.showinfo("Submission", f"Username: {username}\nPassword: {password}\nUser Type: {user_type}")
        else:
            messagebox.showwarning("Incomplete Data", "Please fill in all fields.")

    root = tk.Tk()
    root.title("User Information")
    root.geometry("300x200")

    username_label = tk.Label(root, text="Username:")
    username_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
    username_entry = tk.Entry(root)
    username_entry.grid(row=0, column=1, columnspan=1, padx=10, pady=10)

    password_label = tk.Label(root, text="Password:")
    password_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
    password_entry = tk.Entry(root, show="*")
    password_entry.grid(row=1, column=1, columnspan=1, padx=10, pady=10)

    user_type_label = tk.Label(root, text="User Type:")
    user_type_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")

    user_type_var = tk.StringVar(root)
    user_type_var.set("Admin")

    user_type_dropdown = tk.OptionMenu(root, user_type_var, "Admin", "Teacher", "TA", "Student")
    user_type_dropdown.grid(row=2, column=1, padx=10, pady=10)

    submit_button = tk.Button(root, text="Login", command=login)
    submit_button.grid(row=3, column=1, columnspan=1, padx=10, pady=10, sticky="w")

    exit_button = tk.Button(root, text="Exit", command=root.quit)
    exit_button.grid(row=3, column=1, columnspan=1, padx=10, pady=10, sticky="e")

    root.mainloop()

except Exception as e:
    print("An error occurred:", e)
