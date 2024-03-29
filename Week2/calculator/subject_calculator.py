import tkinter as tk
from tkinter import simpledialog
from Help import HelpPopup


class SubjectCalculator:
    def __init__(self, master):
        self.master = master
        self.subjects = {}  # Dictionary to store subjects and their pass rates
        self.load_help_content()

    def load_help_content(self):
        try:
            with open("Help.txt", "r") as file:
                self.help_content = file.read()
        except FileNotFoundError:
            self.help_content = "Help file not found."
    def run(self):
        self.master.title("Subject Calculator")

        # Help section
        help_label = tk.Label(self.master, text="Help", font=("Arial", 14, "bold"))
        help_label.grid(row=0, column=2, padx=10, pady=5, sticky="e")
        help_text = tk.Text(self.master, width=40, height=20, wrap=tk.WORD)
        help_text.insert(tk.END, self.help_content)
        help_text.config(state=tk.DISABLED)
        help_text.grid(row=1, column=2, rowspan=4, padx=10, pady=5)

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
        subject = self.subject_entry.get().strip()
        pass_rate = self.pass_rate_entry.get().strip()
        if subject and pass_rate:
            subject_info = f"{subject}: {pass_rate}%"
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
            subject, pass_rate = subject_info.split(":")  # Extract the subject name and pass rate
            new_pass_rate = tk.simpledialog.askstring("Edit Pass Rate", f"Enter new pass rate for {subject}:")
            if new_pass_rate:
                self.subjects[subject.strip()] = new_pass_rate.strip()  # Update the pass rate in the dictionary
                self.update_subject_listbox()

    def update_subject_listbox(self):
        self.subject_listbox.delete(0, tk.END)
        for subject, pass_rate in self.subjects.items():
            self.subject_listbox.insert(tk.END, f"{subject}: {pass_rate}%")

def main():
    root = tk.Tk()
    calculator = SubjectCalculator(root)
    calculator.run()
    root.mainloop()

if __name__ == "__main__":
    main()
