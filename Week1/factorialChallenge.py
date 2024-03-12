
# Function to calculate factorial recursively
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
#using a try except to find out errors in the code
try:
    num = int(input("Enter a non-negative number to calculate its factorial: "))
    if num < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        result = factorial(num)
        print(f"The factorial of {num} is: {result}")
        print("This is an integer.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
