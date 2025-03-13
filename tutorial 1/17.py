# 17. Multiplication table of 1 to n numbers
def multiplication_table(n):
    for i in range(1, n + 1):
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")
        print("\n")

print("Multiplication Table:")
multiplication_table(3)