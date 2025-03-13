# 23. Print all prime factors of a number
def prime_factors(n):
    i = 2
    while i * i <= n:
        while n % i == 0:
            print(i, end=" ")
            n //= i
        i += 1
    if n > 1:
        print(n)
print("Prime factors of 56:")
prime_factors(56)