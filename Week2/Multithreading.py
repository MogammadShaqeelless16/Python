"""
Multithreading

Processes and threads may seem like abstract concepts right now, but let's get hands-on and start spinning some up.

Figure 36: Multithreading

The other programmers are going to look at your code and say, "Nice threads." First, import the threading and time modules. So import threading, import time. Then, create a function that calculates the square of a number but takes a really long time to do it. We can call it, appropriately, longSquare. You pass in a number time.sleep for a whole second and then return that number squared. Let's say we want to calculate the square of a few numbers. It will take a long time. For in and range zero through five. This is obviously a fairly contrived example, but these situations often arise in programming.

For instance, waiting to fetch data from a remote server, the code is just sitting around doing nothing, waiting for that data to come back, and this is where threads are so handy. You can do all that waiting in parallel rather than one at a time.

To demonstrate this, make two threads:

t1 is threading.thread and nd
t2 is threading.thread.
Pass in two keyword arguments. The first one is called target, and that's the name of the target function, longSquare. The second is called args. That's going to be the arguments we pass to the function. Copy this and put it there followed by a comma just to show Python that it is a tuple and not a random variable with parentheses around it. If you only have one value in the tuple, sometimes that is necessary.

Start both of the threads with the start function, t1.start t2.start. And finally, join them, t1.join t2.join. This join function checks to see if the thread has completed execution yet and pauses until execution's complete. See this runs in about half the time it would take us to run these one at a time. There is one little problem, where are the results of our function?

Try to get the results from the thread object by saying t1.results return value, but you are not going to find it. The return value of this function is actually nowhere in these threads. There is no way to get the output of this function directly, so here is where we can take advantage of the fact that threads share memory.

Create a results dictionary and bring this code down and modify the function so that that results dictionary gets passed in. Rather than returning anything, it is going to take results and just add it to the dictionary. Pass in results, results. bring that down to keep things organized and finally, print results. There you go! Threads share memory and can modify the same object.

Of course, writing out t1, t2, start, join is laborious if we want lots and lots of values or a variable number of values back. It is a common pattern to put all these into a list, so let's do that. Make a list called threads, plural, and say threading.thread. Target is going to be longSquare, args. It's going to be n, results for n in range 0, 10. Okay, then we need to say t.start for t in threads. Finally, t.join for t in threads and then print results. That was fast. And just for fun, let's do 100 threads. This is so much faster than waiting one at a time.
"""

import threading
import time

# Define a function that calculates the square of a number but takes a long time to do it
def longSquare(n, results):
    # Simulate a long calculation by sleeping for 1 second
    time.sleep(1)
    # Store the result in the results dictionary
    results[n] = n * n

# Create threads for each number from 0 to 9 to calculate their squares
threads = [threading.Thread(target=longSquare, args=(n, results)) for n in range(10)]

# Start all threads
for t in threads:
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

# Print the results
print("Results:", results)
