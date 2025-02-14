import numpy as np
import time


def sieve_of_eratosthenes(limit):
    """Generate a list of prime numbers up to `limit` using the Sieve of Eratosthenes."""
    is_prime = np.ones(limit + 1, dtype=bool)
    is_prime[:2] = False  # 0 and 1 are not prime numbers
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            is_prime[i*i:limit + 1:i] = False
    return np.nonzero(is_prime)[0]

def sum_reciprocals_of_primes_optimized(limit):
    """Sum the reciprocals of all prime numbers up to `limit`."""
    primes = sieve_of_eratosthenes(limit)
    reciprocal_sum = 0.0
    for prime in primes:
        reciprocal_sum += 1 / prime
    return reciprocal_sum
x=time.time()
# Example usage
upper_bound = 1000 # Replace with your desired upper bound
print(f"Sum of reciprocals of primes up to {upper_bound}: {sum_reciprocals_of_primes_optimized(upper_bound)}")
y=time.time()
print(y-x,"s")


