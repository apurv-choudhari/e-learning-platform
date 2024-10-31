import tkinter as tk

def open_flow_window(root):
    root.withdraw()  # Hide the main login window

    flow_window = tk.Toplevel(root)
    flow_window.geometry("500x400")
    flow_window.title("Student Flow")

    back_button = tk.Button(flow_window, text="Back", command=lambda: back_to_login(flow_window, root))
    back_button.pack(pady=10)

    # Centered label displaying flow start message
    message_label = tk.Label(flow_window, text="This is the start of the Student flow", font=("Arial", 14))
    message_label.pack(expand=True)

def back_to_login(flow_window, root):
    flow_window.destroy()
    root.deiconify()
