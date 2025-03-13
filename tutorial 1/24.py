# 24. Print numbers between 100 and 1000 whose sum of digits is divisible by 9
def divisible_by_9():
    for i in range(100, 1001):
        if sum(int(d) for d in str(i)) % 9 == 0:
            print(i, end=" ")
print("Numbers between 100-1000 with digit sum divisible by 9:")
divisible_by_9()