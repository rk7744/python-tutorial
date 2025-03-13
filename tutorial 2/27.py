# 27. Separate prime and composite numbers
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def separate_prime_composite(lst):
    primes, composites = [], []
    for num in lst:
        if is_prime(num):
            primes.append(num)
        else:
            composites.append(num)
    return primes, composites

print(separate_prime_composite([2, 4, 5, 9, 11, 15]))