import hashlib

def hash_password(password):
    """Hashes the given password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def register(username, hashed_password):
    """Registers a new user with the given username and hashed password."""
    try:
        with open("user_credentials.txt", "a") as file:
            file.write(f"{username},{hashed_password}\n")
        print(f"User '{username}' registered successfully.")
    except Exception as e:
        print(f"Error registering user '{username}': {e}")

def login(username, password):
    """Attempts to authenticate the user with the given username and password."""
    try:
        with open("user_credentials.txt", "r") as file:
            for line in file:
                stored_username, stored_password = line.strip().split(',')
                if stored_username == username and hash_password(password) == stored_password:
                    print(f"User '{username}' authenticated successfully.")
                    return True  # Authentication successful
        print(f"Authentication failed for user '{username}'.")
        return False  # Authentication failed
    except Exception as e:
        print(f"Error authenticating user '{username}': {e}")
        return False

# Testing the functions
def test():
    # Testing registration
    register("user1", hash_password("password1"))
    register("user2", hash_password("password2"))

    # Testing login
    print(login("user1", "password1"))  # Should return True
    print(login("user2", "password2"))  # Should return True
    print(login("user3", "password3"))  # Should return False (user not registered)

if __name__ == "__main__":
    test()
