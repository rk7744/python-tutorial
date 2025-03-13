# 6. Remove all occurrences of a substring.
def remove_substring(s, sub):
    return s.replace(sub, '')
print(remove_substring("hello world", "world"))