import tkinter as tk
from tkinter import messagebox
from encryption import hash_password

PASSWORDS_FILE = "passwords.txt"


def show_password_manager():
    # Function to display the password manager screen
    root = tk.Tk()
    root.title("Password Manager")
    # Implement the password manager screen layout and logic here
    root.mainloop()


class PasswordManagerApp:
    def __init__(self, master):
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        # Create your GUI elements here
        self.label = tk.Label(self.master, text="Password Manager")
        self.label.pack()

    def create_card(self, card_name, password):
        # Create a new card with the given name and password
        with open(PASSWORDS_FILE, "a") as file:
            hashed_password = hash_password(password)
            file.write(f"{card_name},{hashed_password}\n")

    def display_cards(self):
        # Display all cards stored in the file
        cards = {}
        try:
            with open(PASSWORDS_FILE, "r") as file:
                for line in file:
                    card_name, encrypted_password = line.strip().split(",")
                    cards[card_name] = encrypted_password
        except FileNotFoundError:
            # Return an empty dictionary if the file doesn't exist yet
            pass
        return cards
