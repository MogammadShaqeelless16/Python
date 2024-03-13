class Person:
    # Constructor method to initialize the object with name and age
    def __init__(self, name, age):
        # Assign the name and age to the object's attributes
        self.name = name
        self.age = age

    # Instance method to greet the person
    def greet(self):
        # Print a personalized greeting message using instance attributes
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    # Instance method to check if a person is an adult
    def is_adult(self):
        # Return True if the person is an adult (age >= 18), False otherwise
        return self.age >= 18

    # Static method to calculate the average age of two people
    @staticmethod
    def average_age(person1, person2):
        # Calculate and return the average age of the two people
        return (person1.age + person2.age) / 2


# Create instances of the Person class
alice = Person("Alice", 30)
bob = Person("Bob", 25)

# Call the greet method on each object
alice.greet()  # Output: Hello, my name is Alice and I am 30 years old.
bob.greet()  # Output: Hello, my name is Bob and I am 25 years old.

# Call the is_adult method on each object
print(alice.is_adult())  # Output: True
print(bob.is_adult())  # Output: True

# Call the static method average_age
average = Person.average_age(alice, bob)
print(f"The average age is: {average}")  # Output: The average age is: 27.5
