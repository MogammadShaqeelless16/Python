import tkinter as tk

class SubjectCalculatorGUI:
    def __init__(self, master, subjects, pass_rates):
        self.master = master
        self.master.title("Subject Calculator")
        self.master.geometry("400x400")
        self.subjects = subjects
        self.pass_rates = pass_rates  # Dictionary to store pass rates

        self.subject_label = tk.Label(master, text="Enter Subject:")
        self.subject_label.pack()

        self.subject_entry = tk.Entry(master)
        self.subject_entry.pack()

        self.pass_rate_label = tk.Label(master, text="Enter Pass Rate:")
        self.pass_rate_label.pack()

        self.pass_rate_entry = tk.Entry(master)
        self.pass_rate_entry.pack()

        self.add_button = tk.Button(master, text="Add Subject", command=self.add_subject)
        self.add_button.pack()

    def add_subject(self):
        subject = self.subject_entry.get()
        pass_rate = float(self.pass_rate_entry.get())
        self.subjects.append(subject)
        self.pass_rates[subject] = pass_rate
        print(self.subjects)
        print(self.pass_rates)



    def enter_student_marks(self):
        pass_rates = self.pass_rates
        student_marks = {}

        for subject in self.subjects:
            mark = simpledialog.askfloat("Enter Marks", f"Enter marks for {subject}:")
            if mark is not None:
                student_marks[subject] = mark

        total_marks = sum(student_marks.values())
        num_subjects = len(student_marks)
        if num_subjects > 0:
            average_mark = total_marks / num_subjects
        else:
            average_mark = 0

        pass_fail_results = {subject: "Pass" if mark >= pass_rates[subject] else "Fail" for subject, mark in student_marks.items()}

        result_message = "\n".join([f"{subject}: {result}" for subject, result in pass_fail_results.items()])
        messagebox.showinfo("Results", f"Pass/Fail results:\n{result_message}\n\nAverage Mark: {average_mark:.2f}")

