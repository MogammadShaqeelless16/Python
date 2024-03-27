"""
Class Inheritance

In the world of computer science and Python programming, it is possible for one class to inherit all the methods and attributes of another class. The original class is referred to as the parent class, while the new class that extends it is known as the child class. This inheritance process happens automatically when the child class is created.

Look at the example: there is a dog class and a chihuahua class needs to be created that inherits from the dog class. To do this, simply write "class Chihuahua(dog):" and include "pass" for now, which creates the new class. A chihuahua instance can then be created using all the methods and attributes of the parent dog class.

However, if the child class defines an attribute or method that is the same as the parent class, the child's version will overwrite the parent's version.

In this example, overwrite the dog class's "speak" method with a more appropriate "yap, yap, yap" method for chihuahuas. You can also add new methods to the child class, like a "wag tail" method, which the chihuahua can use. This is useful when an existing class is used but needs a few changes or additions to it.

Extending Built-in Classes

We can also apply class extensions in Python's built-in classes. In Python, creating a new list can be done by instantiating it as "list". Although it appears as a function, "list" is actually a class.

Suppose you want a list that ensures all appended items are unique, like a set. Create your own unique list class by extending the list class. The unique list class inherits from the list class and we will override the append function.

The new function will check if the item is already in the list and if so, it will return. But remember, we cannot use self.append because it will cause infinite recursion or an endless loop. Instead, call the original append function in the parent class. This is achieved by using the "super" function, which accesses the underlying instance of the parent class, and will be called super.append. To test the new class, create a new instance of the unique list and append some items to it, and then print the list to see that it only records unique items.

Another common scenario where the "super" function is used is in the constructor. If a new attribute is required to be added to our child class instance, this can be done using "self.some_property = unique_list". However, this completely overwrites the constructor of the parent class, which may have some essential initialization requirements.

To avoid this, use "super" again and ensure that the parent constructor is called first before adding our new property. When this new class is initiated, the new property has been added successfully. Although class extensions may seem complicated at first, they are an elegant and powerful tool that can resolve challenging coding issues. Figuring out inheritance requires no legal qualifications!
"""


# Define the parent class Dog
class Dog:
    def speak(self):
        return "Woof!"

# Define the child class Chihuahua inheriting from Dog
class Chihuahua(Dog):
    def speak(self):
        return "Yap, yap, yap!"

    def wag_tail(self):
        return "Wagging tail..."

# Create instances of Dog and Chihuahua classes
dog_instance = Dog()
chihuahua_instance = Chihuahua()

# Call methods from both classes
print(dog_instance.speak())  # Output: "Woof!"
print(chihuahua_instance.speak())  # Output: "Yap, yap, yap!"
print(chihuahua_instance.wag_tail())  # Output: "Wagging tail..."

# Define a unique list class extending from the built-in list class
class UniqueList(list):
    def append(self, item):
        if item not in self:
            super().append(item)
