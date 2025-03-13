# 20. Read and sort list of names alphabetically.
def sort_names():
    names = input("Enter names separated by commas: ").split(',')
    return sorted(names)
print(sort_names())