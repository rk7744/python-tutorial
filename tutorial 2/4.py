# 4. Replace spaces with '*' or '$' if no spaces exist.
def replace_spaces(s):
    return s.replace(' ', '*') if ' ' in s else f'${s}$'
print(replace_spaces("hello world"))