# 10. Sum of even numbers from N given numbers
n = list(map(int, input("Enter numbers: ").split()))
print("Sum of even numbers:", sum(i for i in n if i % 2 == 0))
