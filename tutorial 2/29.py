# 29. Basic set operations
def set_operations(set1, set2):
    return set1.union(set2), set1.intersection(set2), set1.difference(set2)

print(set_operations({1, 2, 3}, {3, 4, 5}))