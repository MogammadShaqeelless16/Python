import hashlib

def hash_password(password):
    """Hashes the given password using a secure hashing algorithm."""
    # Here we'll use SHA-256 algorithm for hashing
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

# You can add more functions for encryption and decryption as needed
