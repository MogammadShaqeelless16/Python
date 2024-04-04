"""
Fundamentals of Threads and Processes

Module 2: Threads and Processes Fundamentals

Earlier in the course it was stated that computers operate on memory. Well, it is a little more complicated than that. An introductory explanation of computational operations might have glossed over some details of how computers really work.

Computers have both memory and file storage. It is like short-term and long-term memory. When we save a file and load to file from the disc, that is in storage i.e. long-term memory. When we declare a variable in our program, that is short-term memory in the processor. It looks a bit like this.

Figure 34: Multiprocessing

So what is the big deal? Why can't we think of both storage and memory as one big blob of accessible data? Well, let's bring in a second program.

The first program saves a file to the disk. The second program, running in a second process, can pick it up. They both have access to the same long-term storage on the physical machine, but if this program writes something to memory, the second program cannot access it.

The operating system is responsible for allocating memory to each process running on the computer. It puts walls between the processes so they cannot access each other's memory. Memory is not one giant vague blob like implied. It is segmented. Access is controlled by the operating system.

Figure to be supplied by Ian

It is very important to a programmer where these things are being stored and who has access to what. But the nifty thing that operating systems allow us to do is to move these two pieces of code into the same process. When we move them into the same process, they get to share memory.

We still get to run them in parallel, at the same time, but instead of separate processes, they are run with separate threads.

Figure 35: Multithreading

A process can have multiple threads and execute code at the same time in parallel. Everything we have been doing in Python so far has been inside a single thread, inside a single process i.e. we compute each statement sequentially, but in this chapter, we are going to start computing things in parallel, inside different threads and processes.

"""

# Example of using threads in Python

import threading
import time

# Define a function to print numbers from 1 to 5
def print_numbers():
    for i in range(1, 6):
        print(i)
        time.sleep(1)  # Sleep for 1 second between each number

# Define a function to print letters from A to E
def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print(letter)
        time.sleep(1)  # Sleep for 1 second between each letter

# Create threads for both functions
numbers_thread = threading.Thread(target=print_numbers)
letters_thread = threading.Thread(target=print_letters)

# Start both threads
numbers_thread.start()
letters_thread.start()

# Wait for both threads to finish
numbers_thread.join()
letters_thread.join()
