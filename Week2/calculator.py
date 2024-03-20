import tkinter as tk
import random  # For random number generation (funny stuff)

# Function to handle button clicks
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

# Function to open a new window with title 'File'
def open_file_window():
    """Opens a new window with a title 'File'."""
    file_window = tk.Toplevel(root)  # Create a new window
    file_window.title("File")
    file_window.resizable(True, True)  # Allow resizing

    # Add some content to the file window (optional)
    # ... (e.g., labels, checkboxes for options)

# Function to open a new window with information about the calculator
def open_about_window():
    """Opens a new window with information about the calculator, centered on the main window."""
    about_window = tk.Toplevel(root)  # Create a new window (use Tk() for separate window)
    about_window.title("About")
    about_window.resizable(False, False)  # Disable resizing

    # Center the "About" window relative to the main window
    about_window.geometry("+{x}+{y}".format(
        x=root.winfo_rootx() + (root.winfo_width() // 2 - about_window.winfo_width() // 2),
        y=root.winfo_rooty() + (root.winfo_height() // 2 - about_window.winfo_height() // 2)
    ))

    # Add content about the calculator
    label = tk.Label(about_window, text="Made by Shaqeel\nWelcome to my weird app!\nThe calculator has some funny stuff happening.\nEnjoy!", font=("Arial", 12))
    label.pack(padx=10, pady=10)

    # Button to close the "About" window
    close_button = tk.Button(about_window, text="Close", command=about_window.destroy)
    close_button.pack(pady=10)

# Main window
logo_path = "logo/calculator_logo.png"  # Replace with your actual path

root = tk.Tk()
root.title("Calculator! Made by Me")

# Load the logo image (assuming correct path)
img = tk.PhotoImage(file=logo_path)
root.iconphoto(True, img)  # Set the logo for the window

# Display for the calculator
display = tk.StringVar()
entry = tk.Entry(root, textvariable=display, font=("Arial", 20), bd=10, insertwidth=4, justify="right")
entry.grid(row=0, column=0, columnspan=4, sticky="ew")

# Button layout
button_info = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3),
    ("=", 5, 0, 4)
]

# Create buttons
for info in button_info:
    text, row, column, *args = info  # Unpack the tuple
    if text == "=":
        button = tk.Button(root, text=text, font=("Arial", 16), command=lambda t=text: button_click(t))
        button.grid(row=row, column=column, columnspan=args[0], sticky="nsew")
    else:
        button = tk.Button(root, text=text, font=("Arial", 16), command=lambda t=text: button_click(t))
        button.grid(row=row, column=column, sticky="nsew")

# Configure columns and rows to resize proportionally
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(6):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()
