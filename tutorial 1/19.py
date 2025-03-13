# 19. Count even and odd numbers in a list
def count_even_odd(lst):
    even_count = sum(1 for x in lst if x % 2 == 0)
    odd_count = len(lst) - even_count
    return even_count, odd_count
print("Even and Odd Count:", count_even_odd([1, 2, 3, 4, 5]))