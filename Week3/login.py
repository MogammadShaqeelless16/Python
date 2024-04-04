import tkinter as tk
from tkinter import messagebox
from encryption import hash_password
from user import login
from password_manager import show_password_manager

PASSWORDS_FILE = "passwords.txt"


def show_login_screen(root):
    # Function to display the login screen
    label_username = tk.Label(root, text="Username:")
    label_username.grid(row=0, column=0)
    entry_username = tk.Entry(root)
    entry_username.grid(row=0, column=1)

    label_password = tk.Label(root, text="Password:")
    label_password.grid(row=1, column=0)
    entry_password = tk.Entry(root, show="*")
    entry_password.grid(row=1, column=1)

    button_login = tk.Button(root, text="Login",
                             command=lambda: login_user(root, entry_username.get(), entry_password.get()))
    button_login.grid(row=2, columnspan=2, pady=10)

    button_register = tk.Button(root, text="Register", command=lambda: show_registration_screen(root))
    button_register.grid(row=3, columnspan=2, pady=10)


def login_user(root, username, password):
    # Function to handle login logic
    if username and password:
        if login(username, hash_password(password)):
            messagebox.showinfo("Success", "Login successful!")
            root.destroy()  # Close the login window
        else:
            messagebox.showerror("Error", "Invalid username or password.")
    else:
        messagebox.showerror("Error", "Please enter both username and password.")


def show_registration_screen(root):
    # Function to display the registration screen
    root_reg = tk.Tk()
    root_reg.title("Registration")
    label_username = tk.Label(root_reg, text="Username:")
    label_username.grid(row=0, column=0)
    entry_username = tk.Entry(root_reg)
    entry_username.grid(row=0, column=1)

    label_password = tk.Label(root_reg, text="Password:")
    label_password.grid(row=1, column=0)
    entry_password = tk.Entry(root_reg, show="*")
    entry_password.grid(row=1, column=1)

    button_register = tk.Button(root_reg, text="Register",
                                command=lambda: register_user(root_reg, entry_username.get(), entry_password.get()))
    button_register.grid(row=2, columnspan=2, pady=10)


def register_user(root, username, password):
    # Function to handle registration logic
    if username and password:
        # Add code here to register the user
        messagebox.showinfo("Success", "Registration successful!")
        root.destroy()  # Close the registration window
    else:
        messagebox.showerror("Error", "Please enter both username and password.")
