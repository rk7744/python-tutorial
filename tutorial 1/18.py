# 18. Check if a number is an Armstrong number
def is_armstrong(n):
    num_str = str(n)
    power = len(num_str)
    return n == sum(int(digit) ** power for digit in num_str)
print("Is 1634 an Armstrong number?", is_armstrong(1634))