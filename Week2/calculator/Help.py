import tkinter as tk

class HelpPopup:
    def __init__(self, master, help_content):
        self.master = master
        self.help_content = help_content
        self.create_help_popup()

    def create_help_popup(self):
        # Help section
        help_label = tk.Label(self.master, text="Help", font=("Arial", 14, "bold"))
        help_label.grid(row=0, column=3, padx=10, pady=5, sticky="e")
        help_text = tk.Text(self.master, width=40, height=20, wrap=tk.WORD)
        help_text.insert(tk.END, self.help_content)
        help_text.config(state=tk.DISABLED)
        help_text.grid(row=1, column=3, rowspan=4, padx=10, pady=5, sticky="e")
