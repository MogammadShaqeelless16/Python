import tkinter as tk
from subject import Subject
from gui import SubjectCalculatorGUI

class SubjectCalculator:
    def __init__(self):
        self.subjects = []

    def run(self):
        root = tk.Tk()
        root.title("Subject Calculator")
        root.geometry("400x300")  # Set fixed window size

        gui = SubjectCalculatorGUI(root, self.subjects)
        root.mainloop()

if __name__ == "__main__":
    calculator = SubjectCalculator()
    calculator.run()
