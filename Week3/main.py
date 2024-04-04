import tkinter as tk
from login import show_login_screen

def main():
    root = tk.Tk()
    root.title("Login")
    show_login_screen(root)
    root.mainloop()

if __name__ == "__main__":
    main()
