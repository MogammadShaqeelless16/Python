import math

# Function to calculate the area of a rectangle
def calculate_rectangle_area(length, width):
    # Formula for rectangle area: length * width
    return length * width

# Function to calculate the area of a circle
def calculate_circle_area(radius):
    # Formula for circle area: π * radius^2
    return math.pi * radius ** 2

# Function to calculate the area of a triangle
def calculate_triangle_area(base, height):
    # Formula for triangle area: 0.5 * base * height
    return 0.5 * base * height

# Function to calculate the area of a square
def calculate_square_area(side_length):
    # Formula for square area: side_length^2
    return side_length ** 2

# Function to draw a rectangle
def draw_rectangle(length, width):
    for i in range(length):
        print("*" * width)

# Function to draw a circle (approximately)
def draw_circle(radius):
    diameter = radius * 2
    for i in range(diameter + 1):
        print(" " * (diameter - int(math.sqrt(radius**2 - (i - radius)**2))) + "*" * (2 * int(math.sqrt(radius**2 - (i - radius)**2)) + 1))

# Function to draw a triangle
def draw_triangle(base, height):
    for i in range(height):
        print(" " * (height - i - 1) + "*" * (2 * i + 1))

# Function to draw a square
def draw_square(side_length):
    for i in range(side_length):
        print("*" * side_length)

# Main function
def main():
    print("Welcome to the Shape Area Calculator!")

    # Menu options
    print("Choose a shape to calculate its area and draw it:")
    print("1. Rectangle")
    print("2. Circle")
    print("3. Triangle")
    print("4. Square")

    # User input for shape selection
    choice = int(input("Enter your choice (1/2/3/4): "))

    # Perform calculations based on user choice
    if choice == 1:  # Rectangle
        length = int(input("Enter the length of the rectangle: "))
        width = int(input("Enter the width of the rectangle: "))
        area = calculate_rectangle_area(length, width)
        print("The area of the rectangle is:", area)
        draw_rectangle(length, width)

    elif choice == 2:  # Circle
        radius = int(input("Enter the radius of the circle: "))
        area = calculate_circle_area(radius)
        print("The area of the circle is:", area)
        draw_circle(radius)

    elif choice == 3:  # Triangle
        base = int(input("Enter the base length of the triangle: "))
        height = int(input("Enter the height of the triangle: "))
        area = calculate_triangle_area(base, height)
        print("The area of the triangle is:", area)
        draw_triangle(base, height)

    elif choice == 4:  # Square
        side_length = int(input("Enter the side length of the square: "))
        area = calculate_square_area(side_length)
        print("The area of the square is:", area)
        draw_square(side_length)

    else:
        print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
