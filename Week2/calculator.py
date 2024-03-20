import tkinter as tk
from tkinter import messagebox

# Function to open a new window for the basic calculator
def open_basic_calculator():
    basic_calculator_window = tk.Toplevel(root)
    basic_calculator_window.title("Basic Calculator")

    # Function to handle button clicks in the basic calculator
    def button_click(symbol):
        """This function handles the button clicks and changes the display."""
        current = display.get()
        if current == "Error":
            display.set("")  # Reset if error
        if symbol == "=":
            try:
                result = eval(current)
                display.set(result)
            except:
                display.set("Error")  # Show error message
        elif symbol == "C":
            display.set("")  # Clear the display
        else:
            display.set(current + symbol)  # Add symbol to display

    # Display for the basic calculator
    display = tk.StringVar()
    entry = tk.Entry(basic_calculator_window, textvariable=display, font=("Arial", 20), bd=10, insertwidth=4, justify="right")
    entry.grid(row=0, column=0, columnspan=4, sticky="ew")

    # Button layout for the basic calculator
    button_info = [
        ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
        ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
        ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
        ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3),
        ("=", 5, 0, 4)
    ]

    # Create buttons for the basic calculator
    for info in button_info:
        text, row, column, *args = info  # Unpack the tuple
        if text == "=":
            button = tk.Button(basic_calculator_window, text=text, font=("Arial", 16), command=lambda t=text: button_click(t))
            button.grid(row=row, column=column, columnspan=args[0], sticky="nsew")
        else:
            button = tk.Button(basic_calculator_window, text=text, font=("Arial", 16), command=lambda t=text: button_click(t))
            button.grid(row=row, column=column, sticky="nsew")

# Function to add a new subject dynamically
def add_subject():
    new_subject = subject_entry.get()
    new_pass_rate = pass_rate_entry.get()
    if new_subject and new_pass_rate:
        try:
            pass_rate = float(new_pass_rate)
            if 0 <= pass_rate <= 100:
                subject_labels.append((new_subject, pass_rate))
                subject_label = tk.Label(subjects_frame, text=f"{new_subject} (Pass Rate: {pass_rate}%)")
                subject_label.pack()
                subject_entry.delete(0, tk.END)
                pass_rate_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Pass rate must be between 0 and 100")
        except ValueError:
            messagebox.showerror("Error", "Pass rate must be a valid number")
    else:
        messagebox.showerror("Error", "Please enter both subject name and pass rate")

# Function to calculate average mark
def calculate_average_mark():
    total_marks = 0
    total_weight = 0
    for subject, pass_rate in subject_labels:
        mark = subject_marks.get(subject, 0)
        total_marks += mark
        total_weight += pass_rate * mark / 100
    if total_weight == 0:
        messagebox.showwarning("Warning", "No subjects added or marks entered")
    else:
        average_mark = total_marks / total_weight
        messagebox.showinfo("Average Mark", f"The average mark is: {average_mark:.2f}")

# Main window for the subject calculator
root = tk.Tk()
root.title("Subject Calculator")

# Frame for subjects
subjects_frame = tk.Frame(root)
subjects_frame.pack()

# Entry for adding new subjects
subject_entry = tk.Entry(root)
subject_entry.pack()

# Entry for adding pass rates
pass_rate_entry = tk.Entry(root)
pass_rate_entry.pack()

# Button to add a new subject
add_subject_button = tk.Button(root, text="Add Subject", command=add_subject)
add_subject_button.pack()

# Button to calculate average mark
calculate_button = tk.Button(root, text="Calculate Average Mark", command=calculate_average_mark)
calculate_button.pack()

# List to store subject labels
subject_labels = []

# Dictionary to store subject marks
subject_marks = {}

# Menu bar for the basic calculator
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Add menu items
calculator_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Calculator", menu=calculator_menu)
calculator_menu.add_command(label="Open Basic Calculator", command=open_basic_calculator)

root.mainloop()
