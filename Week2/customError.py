"""
Working With Custom Exceptions

Custom exceptions is an easy one. In fact, you already know how to do this, class CustomException extends Exception:pass. Now you have written a custom exception.

There are, however, a few more things to cover. The pass statement is used because we literally do not need to define anything for our new CustomException class. It inherits the constructor of the Exception class that it is extending.

The key information is in the name, CustomException and often, this is all the information you need to know to help debug your app or let the user know what they are doing wrong.

We can write a function that raises this new CustomException, def causeError:raise CustomException and then call the function. Notice the CustomException error class in the name, then there's this colon, and then after that, it is curiously blank. Pass a custom message into the new class. You called the causeError function and see that message gets printed out.

Custom exceptions are usually lightweight classes with very little in the way of special attributes and methods and things, but might have some attributes that are useful for organizing and presenting information to the user about the error. For example, if you are writing a web server and need to raise HTTP exceptions at various points in the code, you might have an HttpException class and various specific HttpException classes that extend it.

Adding Attributes

Here is the HttpException. It is going to extend the Exception and we are going to give it a status code. Make that None for now — a special None value, and a message that is also None. Then override the parent constructor by defining our own constructor and then when we call that parent constructor. Pass in the status code message, is statusCode and the message is self.statusCode. Write a few child classes that extend the HttpException, NotFound HttpException. All we need to do here is define our status code, which is going to be 404, and our message which is going to be Resource not found.

Write a ServerError class, class ServerError extends HttpException statusCode 500 and message: This server messed up! Great. Then write a function that raises a ServerError, raiseServerError raise ServerError, and then call it. Notice that this exception message gets formatted with our status code and message because it extends this HttpException.

Writing custom exception classes is a great way to keep your code clean and organized. These classes act as documentation for all the problems that could happen, what cause them, what the solutions are, and they also separate common expected errors from something perhaps really bad that requires developer attention.
"""

# Define a custom exception class
class CustomException(Exception):
    pass

# Define a function to raise the custom exception
def causeError():
    raise CustomException("This is a custom exception message.")

# Test the custom exception
causeError()

# Define an HTTP exception class with attributes
class HttpException(Exception):
    def __init__(self, status_code=None, message=None):
        self.status_code = status_code
        self.message = message
        super().__init__(self.message)

# Define child classes extending HttpException
class NotFound(HttpException):
    def __init__(self):
        super().__init__(status_code=404, message="Resource not found.")

class ServerError(HttpException):
    def __init__(self):
        super().__init__(status_code=500, message="This server messed up!")

# Define a function to raise a ServerError
def raiseServerError():
    raise ServerError()

# Test raising a ServerError
raiseServerError()
