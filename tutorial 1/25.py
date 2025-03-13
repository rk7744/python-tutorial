# 25. Find X^Y without using pow() or **
def power(x, y):
    result = 1
    for _ in range(y):
        result *= x
    return result

print("3^4 without pow():", power(3, 4))