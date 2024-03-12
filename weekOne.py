#First line of Code
print('hello word')

# Introduction
print("Hello there! Let's explore some basics of Python together.")

# Personal Information
name = "Shaqeel"
age = 24
profession = "Graduate Capaciti Intern"
is_married = False

# Displaying Personal Information
print(f"My name is {name}.")
print(f"I am {age} years old and work as a {profession}.")
if is_married:
    print("I am happily married.")
else:
    print("I am single and loving it!")

# Arithmetic Operations
num1 = 15
num2 = 7
print("Let's do some math:")
print(f"{num1} + {num2} =", num1 + num2)
print(f"{num1} - {num2} =", num1 - num2)
print(f"{num1} * {num2} =", num1 * num2)
print(f"{num1} / {num2} =", num1 / num2)

# Favourite Things
favorite_foods = ['pizza', 'chocolate', 'ice cream']
print("My favorite foods are:", ', '.join(favorite_foods))

# Conditional Statement
current_season = "winter"
if current_season == "winter":
    print("It's cold outside! Don't forget your jacket.")
elif current_season == "summer":
    print("Time for some fun in the sun!")
else:
    print("Enjoy the beautiful weather!")

# Looping
print("Let's count to 5:")
for i in range(1, 6):
    print(i)

# Farewell
print("Thanks for exploring Python with me. Happy coding!")
