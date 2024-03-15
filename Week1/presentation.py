import tkinter as tk

class LoopAnimation:
    def __init__(self, master):
        # Initialize the main window
        self.master = master
        self.master.title("Loop Animation")

        # Create canvas for animation
        self.canvas = tk.Canvas(self.master, width=400, height=300, bg="white")
        self.canvas.pack()

        # Create a walking man on the canvas
        self.man = self.canvas.create_rectangle(20, 150, 70, 200, fill="blue")  # Head
        self.body = self.canvas.create_rectangle(40, 200, 50, 300, fill="blue")  # Body
        self.leg1 = self.canvas.create_rectangle(40, 300, 45, 350, fill="blue")  # Leg 1
        self.leg2 = self.canvas.create_rectangle(55, 300, 60, 350, fill="blue")  # Leg 2
        self.arm1 = self.canvas.create_rectangle(20, 200, 30, 250, fill="blue")  # Arm 1
        self.arm2 = self.canvas.create_rectangle(60, 200, 70, 250, fill="blue")  # Arm 2

        self.dx = 2  # Horizontal movement speed
        self.dy = 0  # Vertical movement speed
        self.is_animating = False  # Flag to control animation state
        self.iterations = 0  # Counter for loop iterations

        # Labels for loop explanations
        self.label_while = tk.Label(self.master, text="While loop: 'while condition:'")
        self.label_while.pack(pady=(10,0))

        self.label_for = tk.Label(self.master, text="For loop: 'for item in iterable:'")
        self.label_for.pack(pady=(10,0))

        # Display iteration count
        self.iteration_label = tk.Label(self.master, text="Iterations: 0")
        self.iteration_label.pack(pady=(10,0))

        # Start buttons for while and for loops
        self.start_while_button = tk.Button(self.master, text="Start While Loop", command=self.start_while_loop)
        self.start_while_button.pack(side=tk.LEFT, padx=10)

        self.start_for_button = tk.Button(self.master, text="Start For Loop", command=self.start_for_loop)
        self.start_for_button.pack(side=tk.LEFT, padx=10)

    def start_while_loop(self):
        # Start the while loop animation
        self.is_animating = True
        self.iterations = 0
        self.iteration_label.config(text="Iterations (While Loop): 0")
        self.while_loop_animation()

    def start_for_loop(self):
        # Start the for loop animation
        self.is_animating = True
        self.iterations = 0
        self.iteration_label.config(text="Iterations (For Loop): 0")
        self.for_loop_animation()

    def while_loop_animation(self):
        # While loop animation
        while self.is_animating and self.iterations < 10:
            self.move_man()
            self.iterations += 1
            self.iteration_label.config(text=f"Iterations (While Loop): {self.iterations}")
            self.master.update()
            self.master.after(100)  # Delay between iterations

    def for_loop_animation(self):
        # For loop animation
        for i in range(10):  # Iterate 10 times
            if not self.is_animating:
                break
            self.move_man()
            self.iterations += 1
            self.iteration_label.config(text=f"Iterations (For Loop): {self.iterations}")
            self.master.update()
            self.master.after(500)  # Delay between iterations

    def move_man(self):
        # Function to move the man
        self.canvas.move(self.man, self.dx, self.dy)
        self.canvas.move(self.body, self.dx, self.dy)
        self.canvas.move(self.leg1, self.dx, self.dy)
        self.canvas.move(self.leg2, self.dx, self.dy)
        self.canvas.move(self.arm1, self.dx, self.dy)
        self.canvas.move(self.arm2, self.dx, self.dy)
        pos = self.canvas.coords(self.man)
        if pos[2] >= 400 or pos[0] <= 0:
            self.dx *= -1
        self.iterations += 1

def main():
    # Create the main window
    root = tk.Tk()
    app = LoopAnimation(root)
    root.mainloop()

if __name__ == "__main__":
    main()
