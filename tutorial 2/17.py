# 17. Compute sin(x) using Taylor series.
def sin_taylor(x, n):
    from math import factorial
    return sum(((-1)**i * x**(2*i + 1)) / factorial(2*i + 1) for i in range(n))
print(sin_taylor(1.57, 5))