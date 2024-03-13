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


class Student(Person):
    # Constructor method to initialize the student object with name, age, and student ID
    def __init__(self, name, age, student_id):
        # Call the parent class constructor to initialize name and age
        super().__init__(name, age)
        # Assign the student ID to the student object's attribute
        self.student_id = student_id

    # Instance method to display student information
    def display_student_info(self):
        # Call the greet method from the parent class
        self.greet()
        # Print the student ID
        print(f"I am a student with ID: {self.student_id}")


# Create an instance of the Student class
student1 = Student("Alice", 20, "12345")

# Call the display_student_info method on the student1 object
student1.display_student_info()


# In this example:

# We define a Person class with a constructor method __init__ and an instance method greet.
# We define a Student class that inherits from the Person class.
# The Student class has its own constructor method __init__ that calls the parent class constructor using super().__init__,
# and it also has an instance method display_student_info to display student information.
# We create an instance of the Student class named student1.
# We call the display_student_info method on the student1 object, which invokes the greet method inherited from the Person class
# and prints additional student information.