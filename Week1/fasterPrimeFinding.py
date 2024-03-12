def all_primes_up_to(n):
    """
    Generate a list of prime numbers up to the specified limit (inclusive).
    Args:
    - n (int): The upper limit for finding prime numbers.

    Returns:
    - list: A list of prime numbers up to the specified limit.
    """
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        # Check divisibility up to the square root of the current number
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

# User input for the upper limit
try:
    limit = int(input("Enter the upper limit to find prime numbers up to: "))
    if limit < 2:
        print("Please enter a number greater than or equal to 2.")
    else:
        prime_numbers = all_primes_up_to(limit)
        print(f"Prime numbers up to {limit}: {prime_numbers}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
