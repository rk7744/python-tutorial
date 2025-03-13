# 31. Completely remove duplicate elements without keeping any copy
def remove_all_duplicates(lst):
    from collections import Counter
    count = Counter(lst)
    return [item for item in lst if count[item] == 1]

print(remove_all_duplicates([1, 2, 2, 3, 4, 4, 5]))
