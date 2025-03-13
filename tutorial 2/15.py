# 15. Compute nCr using factorial.
def nCr(n, r):
    from math import factorial
    return factorial(n) // (factorial(r) * factorial(n - r))
print(nCr(5, 2))