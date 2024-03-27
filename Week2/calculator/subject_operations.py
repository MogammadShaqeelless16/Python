import tkinter as tk
from tkinter import simpledialog

class SubjectOperations:
    def __init__(self, master, subjects):
        self.master = master
        self.subjects = subjects

    def create_subject_calculator_ui(self):
        # Create labels and entry boxes for adding subjects and their pass rates
        tk.Label(self.master, text="Add Subject:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.subject_entry = tk.Entry(self.master)
        self.subject_entry.grid(row=0, column=1, padx=10, pady=5)
        tk.Label(self.master, text="Pass Rate:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.pass_rate_entry = tk.Entry(self.master)
        self.pass_rate_entry.grid(row=1, column=1, padx=10, pady=5)

        # Button to add subject
        add_button = tk.Button(self.master, text="Add Subject", command=self.add_subject)
        add_button.grid(row=2, column=0, columnspan=2, pady=10)

        delete_button = tk.Button(self.master, text="Delete Subject", command=self.delete_subject)
        delete_button.grid(row=4, column=0, pady=10, sticky="ew")

        # Button to edit subject
        edit_button = tk.Button(self.master, text="Edit Pass Rate", command=self.edit_subject)
        edit_button.grid(row=4, column=1, pady=10, sticky="ew")

        edit_button = tk.Button(self.master, text="Edit", command=self.edit_subject)
        edit_button.grid(row=6, column=0, columnspan=2, pady=10)

        # Listbox to display added subjects and their pass rates
        self.subject_listbox = tk.Listbox(self.master)
        self.subject_listbox.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")

    def add_subject(self):
        subject = self.subject_entry.get()
        pass_rate = self.pass_rate_entry.get()
        if subject and pass_rate:
            self.subjects[subject] = pass_rate
            self.update_subject_listbox()

    def delete_subject(self):
        selection = self.subject_listbox.curselection()
        if selection:
            subject_info = self.subject_listbox.get(selection[0])  # Get the subject info from the listbox
            subject = subject_info.split(":")[0]  # Extract the subject name
            if subject in self.subjects:
                del self.subjects[subject]
                self.update_subject_listbox()

    def edit_subject(self):
        selection = self.subject_listbox.curselection()
        if selection:
            subject_info = self.subject_listbox.get(selection[0])  # Get the selected subject info from the listbox
            subject, pass_rate = subject_info.split(":")  #
