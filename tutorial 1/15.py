# 15. Prime numbers less than 1000
primes = [x for x in range(2, 1000) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))]
print("Prime numbers less than 1000:", primes)