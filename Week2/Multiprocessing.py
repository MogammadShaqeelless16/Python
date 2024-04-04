"""
Multiprocessing

You are probably great at multi-processing and Python already and don't even know it. There is a file called 1000seconds.py. All it does is call time.sleep for a thousand seconds. Open a second tab and run it in the second tab. Now we have two tabs running this program. Two Python processes running independently on your machine, multi-processing, and Python.

Yes, you can have two separate Python processes running but you have to start them by hand. How do we write a program to start, stop, and manage these for us? Well, conveniently, there is a module that is very similar to the threading module we used previously. That module is called multiprocessing.

Figure 37: Multiprocessing

From multiprocessing import Process. Before you run this, there is a small hitch with using the official Python multiprocessing module.

On some operating systems, you cannot use this to spin up a new process that runs the function if that function is defined in the same file as opposed to imported at the top, like this, import myFunction. That is going to make life difficult for us where we want to define and run functions in the same Jupyter Notebook. Fortunately, there is a third-party module that solves this called multiprocess and you can install it with pip install multiprocess.

The multiprocess module has all of the same functions and is used exactly the same as multiprocessing but it does not have the bug with pickiness about where the function is defined. So play around with it, and use either of them for these examples, but we are going to use multiprocess and also import the time module.

This process class is so similar to the thread class that was used previously and that code can simply be copied and pasted down here. Now, instead of threading.thread, we want process. So replace both of those and instead of t1 and t2, call them p1 and p2. This should work exactly the same now but there are no results.

Remember, processes do not share memory. They get a copy of this dictionary in their own separate memory space, and we have no way of accessing it except if they record it somewhere like a file system or a database. One thing we can do is print the computed value from within the function itself. Rather than returning this or saving it in the results, we just print. But it printed them right next to each other, not a 14, it is a one and a four. What happens if we add another line in here, like Finished computing?

It is printing the one and the four very quickly, then it prints both processes, print Finished computing, and then we have this extra weird new line. Well, what happens if we add 10 processes to the mix? Again, use the same pattern that was used previously with the threads. Processes are equal to a list, n for n in range (0,10) then p.start, p for in processes, and p.join p for p in processes and we don't need to bother printing the results. See this output starts to look a little bit funky.
"""

import time
from multiprocess import Process

# Define a function that calculates the square of a number but takes a long time to do it
def longSquare(n):
    # Simulate a long calculation by sleeping for 1 second
    time.sleep(1)
    # Print the result
    print(n * n, "Finished computing")

# Create processes for each number from 0 to 9 to calculate their squares
processes = [Process(args=(n,)) for n in range(10)]

# Start all processes
for p in processes:
    p.start()

# Wait for all processes to finish
for p in processes:
    p.join()
