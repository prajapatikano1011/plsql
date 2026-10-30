# Practical 53: Remove all prime numbers from a list of 20 numbers

nums = [2, 3, 4, 7, 9, 11, 14, 15, 17, 18, 19, 21, 23, 24, 27, 29, 30, 31, 33, 35]

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

non_primes = [x for x in nums if not is_prime(x)]

print("Original list of 20 numbers:", nums)
print("List after removing primes:", non_primes)
