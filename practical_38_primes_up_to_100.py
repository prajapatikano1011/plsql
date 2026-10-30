# Practical 38: List of prime numbers up to 100

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = [x for x in range(2, 101) if is_prime(x)]
print("Prime numbers up to 100:")
print(primes)
