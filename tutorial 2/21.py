# 21. Sum of all even numbers in a group of n numbers.
def sum_even_numbers():
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
    return sum(num for num in nums if num % 2 == 0)
print(sum_even_numbers())