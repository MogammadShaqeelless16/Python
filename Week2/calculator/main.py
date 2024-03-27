import tkinter as tk
from subject_calculator import SubjectCalculator

def main():
    root = tk.Tk()
    calculator = SubjectCalculator(root)  # Pass the root widget as an argument
    calculator.run()
    root.mainloop()

if __name__ == "__main__":
    main()