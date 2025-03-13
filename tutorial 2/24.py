# 24. Finding the mode of a list of numbers
def find_mode(numbers):
    from collections import Counter
    count = Counter(numbers)
    mode = max(count, key=count.get)
    return mode

print(find_mode([1, 2, 2, 3, 4, 4, 4, 5]))
