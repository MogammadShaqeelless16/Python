"""
Practice Exercise 2: Extending the Messenger

Summary:
In this exercise, we learn about exchanging messages between senders and receivers in programming. The Messenger class includes a send method that sends messages to listeners, which are other Messenger classes or subclasses. We're tasked with completing the SaveMessages class, which collects and stores messages along with their received times. Additionally, we need to implement a printMessages function to display stored messages with formatting.

Solution Summary:
Congratulations on completing the challenge! The key is to store messages as a property of the SaveMessages class and utilize a helper function to get the current time. Messages are stored in a list or dictionary along with their timestamps. The printMessages function prints out the stored messages with formatting. Remember to clear the list of messages after printing to avoid duplicates.

Example:
# Create instances of Messenger and SaveMessages classes


# Print stored messages along with their received times

"""

# You can copy this content into a Python file named MessengerExerciseSummary.py
# or any other name you prefer and include it in your IDE project.
messenger1 = Messenger()
save_messages = SaveMessages([messenger1])

# Send a message using the send method
messenger1.send("Hello, world!")
save_messages.printMessages()