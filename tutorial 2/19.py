# 19. n-th Fibonacci number using recursion.
def fibonacci(n):
    if n <= 1: return n
    return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(7))