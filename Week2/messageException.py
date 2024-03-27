"""
Learning Activities

Practice Exercise 3: Message Exceptions

This challenge has three parts. But, before you raise any exceptions, read carefully. Comments were added in each part of the code that should be modified, and the three parts of the challenge have also been outlined at the top.

Writing and handling exceptions are not as easy as filling out a single function and seeing if it runs. It is a practice that intertwines itself with and throughout the existing code. So, what could be better? Use existing code.

Use the messenger and save messages classes from the previous challenge, and also add a concept of max messages or the maximum number of messages that the save messages class can hold. When print messages are called, it flushes the list, the list of messages, sets it back to an empty list, and then messages can be added again.

Your challenge here, in three parts, is to:

1. Finish filling out this too many exceptions class.
2. Then raise that too many messages exception if too many messages are added.
3. Finally, handle that exception appropriately and make sure that all the messages get printed out.

Now go forth and write something exceptional.

Practice Exercise 3: Message Exception Solution

The first thing you want to do is make your too many messages exception class extend the Python exception class. Then add super dot in it with some sort of message explaining what happened. Next, you want to make sure that you raise that exception in the receive method here. Modify this loop to catch that too many messages exception. You want to print all the messages and then resend them.

Finally, outside the loop, we want to make sure that we print any remaining messages inside our listener class. If you go through and run these, you should have all of them.
"""

# Define a custom exception class for too many messages
class TooManyMessagesException(Exception):
    def __init__(self, message="Too many messages."):
        super().__init__(message)

# Define the SaveMessages class with a maximum message limit
class SaveMessages:
    def __init__(self, max_messages=10):
        self.messages = []
        self.max_messages = max_messages

    def receive(self, message):
        if len(self.messages) >= self.max_messages:
            raise TooManyMessagesException()
        self.messages.append(message)

    def print_messages(self):
        for message in self.messages:
            print(message)
        self.messages = []

# Define the Messenger class with a listener and message sending functionality
class Messenger:
    def __init__(self):
        self.listener = None

    def add_listener(self, listener):
        self.listener = listener

    def send_message(self, message):
        if self.listener:
            self.listener.receive(message)

# Define a listener class that handles receiving and printing messages
class Listener:
    def __init__(self, name):
        self.name = name
        self.messages = []

    def receive(self, message):
        self.messages.append(message)

    def print_received_messages(self):
        for message in self.messages:
            print(message)
        self.messages = []

# Instantiate the SaveMessages class and set a maximum message limit
save_messages = SaveMessages(max_messages=5)

# Instantiate the Messenger and Listener classes
messenger = Messenger()
listener = Listener("John")

# Add the listener to the messenger
messenger.add_listener(listener)

# Send messages using the messenger
messages_to_send = ["Message 1", "Message 2", "Message 3", "Message 4", "Message 5", "Message 6"]
for message in messages_to_send:
    try:
        messenger.send_message(message)
    except TooManyMessagesException as e:
        print(e)
        save_messages.print_messages()

# Print any remaining messages in the listener
listener.print_received_messages()
