import tkinter as tk
from subject_calculator import SubjectCalculator

def main():
    root = tk.Tk()
    calculator = SubjectCalculator(root)
    calculator.run()
    root.mainloop()

if __name__ == "__main__":
    main()
