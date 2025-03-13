# 28. Sum of odd numbers within a range
def sum_of_odds(lower, upper):
    return sum(i for i in range(lower, upper + 1) if i % 2 != 0)
print("Sum of odd numbers between 1 and 10:", sum_of_odds(1, 10))