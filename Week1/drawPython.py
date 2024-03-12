import tkinter as tk

def draw(event):
    x, y = event.x, event.y
    canvas.create_oval(x, y, x+5, y+5, fill=current_color)

def change_color(new_color):
    global current_color
    current_color = new_color

# Create main window
root = tk.Tk()
root.title("Simple Drawing")

# Create canvas widget
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack(expand=tk.YES, fill=tk.BOTH)

# Create toolbox for colors
color_box = tk.Frame(root)
color_box.pack(side=tk.BOTTOM, fill=tk.X)

colors = ["red", "green", "blue", "black"]
current_color = "black"

for color in colors:
    color_button = tk.Button(color_box, bg=color, width=3, command=lambda c=color: change_color(c))
    color_button.pack(side=tk.LEFT)

# Bind mouse click event to draw function
canvas.bind("<B1-Motion>", draw)

# Run the application
root.mainloop()
