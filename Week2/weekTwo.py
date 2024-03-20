# Define a function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Main program
if __name__ == "__main__":
    # Define a list of numbers
    numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

    # Print prime numbers from the list using a loop and the is_prime function
    print("Prime numbers from the list:")
    for num in numbers:
        if is_prime(num):
            print(num)

    # Calculate the factorial of a number using a function
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)

    # Print factorial of numbers from 1 to 5
    print("\nFactorials of numbers from 1 to 5:")
    for i in range(1, 6):
        print(f"{i}! =", factorial(i))

    # Check the data type of a variable using an if statement
    x = 10
    if type(x) == int:
        print("\nThe variable x is of type int.")
    elif type(x) == float:
        print("\nThe variable x is of type float.")
    elif type(x) == str:
        print("\nThe variable x is of type str.")
