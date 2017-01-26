def is_prime(m):
    """Checks if the argument is a prime number."""

    if m < 2: return False

    for i in range(2, m):
        if m % i == 0:
            return False

    return True

def get_largest_prime_factor(k):
    """Gets the largest prime factor for the argument."""

    prime_divide = (p for p in range(1, k))
    for d in prime_divide:

        if k % d == 0 and is_prime(k / d):
            return k / d

print (get_largest_prime_factor(234))