# 26. Separate integers, floats, and strings
def separate_types(lst):
    integers, floats, strings = [], [], []
    for item in lst:
        if isinstance(item, int):
            integers.append(item)
        elif isinstance(item, float):
            floats.append(item)
        elif isinstance(item, str):
            strings.append(item)
    return integers, floats, strings

print(separate_types([1, 2.5, 'hello', 3, 4.7, 'world']))
