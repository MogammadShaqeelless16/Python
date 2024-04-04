import tkinter as tk
from tkinter import messagebox
from user import register, hash_password

class RegisterWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.title("Register")
        self.geometry("300x150")

        self.label_username = tk.Label(self, text="Username:")
        self.label_username.pack()
        self.entry_username = tk.Entry(self)
        self.entry_username.pack()

        self.label_password = tk.Label(self, text="Password:")
        self.label_password.pack()
        self.entry_password = tk.Entry(self, show="*")
        self.entry_password.pack()

        self.button_register = tk.Button(self, text="Register", command=self.register_user)
        self.button_register.pack(pady=10)

    def register_user(self):
        username = self.entry_username.get().strip()
        password = self.entry_password.get().strip()

        if username and password:
            # Hash the password before registration
            hashed_password = hash_password(password)
            register(username, hashed_password)
            messagebox.showinfo("Success", "Registration successful!")
            self.destroy()
        else:
            messagebox.showerror("Error", "Please enter both username and password.")
