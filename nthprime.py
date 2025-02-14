from sympy import prime
def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while p * p <= limit:
        if is_prime[p]:
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p, prime in enumerate(is_prime) if prime]

def get_nth_prime(n):
    # Estimate an upper bound for the nth prime number
    if n < 6:
        upper_bound = 15
    else:
        upper_bound = int(n * (log(n) + log(log(n))))
    
    primes = sieve_of_eratosthenes(upper_bound)
    if n <= len(primes):
        return primes[n - 1]
    else:
        raise ValueError("Upper bound for the sieve was too low.")

# Example usage
from math import log

n = 100
  # For example, to get the 10th prime number
print(f"{get_nth_prime(n)}, yes its indeed prime" if get_nth_prime(n)==prime(n) else f"{get_nth_prime(n)}, this is a mistake, its not prime!")

