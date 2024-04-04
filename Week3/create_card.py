import tkinter as tk
from password_manager import create_card


class CreateCardWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.title("Create Card")
        self.geometry("300x150")

        self.label_card_name = tk.Label(self, text="Card Name:")
        self.label_card_name.pack()
        self.entry_card_name = tk.Entry(self)
        self.entry_card_name.pack()

        self.label_password = tk.Label(self, text="Password:")
        self.label_password.pack()
        self.entry_password = tk.Entry(self, show="*")
        self.entry_password.pack()

        self.button_create = tk.Button(self, text="Create", command=self.create_card)
        self.button_create.pack(pady=10)

    def create_card(self):
        card_name = self.entry_card_name.get().strip()
        password = self.entry_password.get().strip()

        if card_name and password:
            create_card(card_name, password)
            # Optionally, provide feedback to the user
            self.destroy()
        else:
            # Optionally, provide error message for invalid input
            pass
