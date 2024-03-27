# Define a class called "Person"
class Person:
    # Constructor method to initialize the object with name and age
    def __init__(self, name, age):
        # Assign the name and age to the object's attributes
        self.name = name
        self.age = age


    # Method to greet the person
    def greet(self):
        # Print a personalized greeting message
        print("Hello, my name is {self.name} and I am {self.age} years old.")


# Create an instance of the Person class with name "Alice" and age 30
alice = Person("Shaqeel", 30)

# Create another instance of the Person class with name "Bob" and age 25
bob = Person("Bob", 25)

# Call the greet method on the alice object
alice.greet()  # Output: Hello, my name is Alice and I am 30 years old.

# Call the greet method on the bob object
bob.greet()  # Output: Hello, my name is Bob and I am 25 years old.
