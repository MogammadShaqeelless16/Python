"""
Managing and Handling Exceptions

Exceptions are not to be feared but they do need to be reigned in. We saw a little bit about how to do this previously with the Try / Except statement. Here we are catching this exception and then just returning it.

We do not get a stack trace or anything, but do see that this zero division error instance is returned. There are a few interesting things you can do with this Try / Except pattern. For instance, if we do not care about getting the specific instance of the exception, and just want to print something, we do not have to have the as e in order to catch an exception. There was some sort of error and then that just prints out.

Finally

Another useful tool is the finally statement. If you take the Try / Except block and add a finally to it, this will always execute and gets printed out.

Finally statements can be useful because they will always execute no matter what happens inside this try block. You do not even need any except statements! This error is thrown, but still printed out. Even if no exception is raised at all, that still executes. Often this is used when timing how long a function takes to execute. So if we import the time class, import time, this can be used to actually time our function.

Now make a timer. We need the start time, time.time will give you the current time and seconds. In the finally statement, make this an f-string and say, Function took, time.time minus start seconds to execute. Another fun thing to do with this is time.sleep. And time.sleep just pauses execution for a number of seconds. In this case, pause it for half a second. So you can see that half-second followed by very fast execution. If the statement is changed to something that causes a zero division error, that timer still happens.

This try-finally pattern keeps the code clean and compact, and lets you do any needed cleanup or logging after a statement completes no matter what happens inside the try block.

Catching Exceptions by Type

Notice that you are always catching this exception class. You could add another except statement above this and chain these together just fine.

We are going to catch the zero division specifically. There was a zero division error, and now that prints out. A type error statement can also be added, except type error and printed. But of course, there was a zero division error, not a type error.

Let's cause a type error by trying to add an int to string. This should result in a type error. The order of these except statements does matter here and Python will try the first one. If you move the general exception up, this is the class from which all of these extend, there was some sort of error.

You always want the most general exceptions down here and then the more specific ones up top. Sometimes you are doing really involved exception handling and catching. For instance, this is seen quite often with HTTP request-response handling where there are a lot of different types of HTTP errors and there are many except statements in a row. Simply copy and paste all of these different blocks into many different functions. In this situation, it can be really handy to move this trying and catching into a single function.

Custom Decorators

Custom decorators can also be used to do this. We saw decorators previously with the static method decorator but now we are going to write our own.

Grab all these exception handlings that were done and make a new function called handleException. We are going to pass as an argument, a function, and then define an inner function called wrapper. Try to execute this function that was passed in and then paste the exceptions here. Now return this wrapper function.

Make a decorator handleException and put it on a causeError function. This is just going to return one over zero. If we call causeError, this handle exception was used to accept those various exceptions that this could throw. This decorator can certainly be reused for another function.

Raising Exceptions

Let's talk about raising exceptions. Use the handle exception decorator. Make a function called raiseError raise Exception. This raise statement raises or throws this new exception that was created when it is reached.

For instance, we can turn this into a function that excepts any input except the number zero. Add an argument and say if n is equal to zero, we raise an exception. Otherwise, we print n. Notice that an else statement is not used. This is not needed because once the exception is raised, this execution will halt, and throw this exception and then the print n will never be reached. We, therefore, do not need an else statement there.

Now there is one problem with this. Notice in the handleException function, this is the function that gets passed in, this raiseErrors being passed in, but when we call it, there are no arguments even though our function has an argument. We are now trying to use this handler on a function that takes arguments. So, we need to modify it somewhat using the variable args and we can pass our args to this function.

When we rerun that, there is some sort of error. We get an error printed out if the argument we pass in is zero, otherwise it just prints out the value. Writing your functions to be able to raise exceptions is especially powerful when you combine it with custom exceptions. So let's go take a look at those next.
"""

# Define a function to handle exceptions
def handleException(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ZeroDivisionError:
            print("There was a ZeroDivisionError.")
        except TypeError:
            print("There was a TypeError.")
    return wrapper

# Define a function to cause an error
@handleException
def causeError(n):
    if n == 0:
        raise Exception("Number cannot be zero.")
    else:
        print(n)

# Test the error-causing function
causeError(5)  # Output: 5
causeError(0)  # Output: "There was a ZeroDivisionError."
causeError('a')  # Output: "There was a TypeError."
