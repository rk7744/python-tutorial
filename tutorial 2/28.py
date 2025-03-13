# 28. Sort a list in non-decreasing order without built-in functions
def custom_sort(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst

print(custom_sort([5, 1, 9, 3, 7]))