# 14. First 10 Fibonacci numbers
fib = [0, 1]
for _ in range(8):
    fib.append(fib[-1] + fib[-2])
print("Fibonacci:", fib)
