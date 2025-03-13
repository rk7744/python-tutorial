# 5. Slice string into odd and even indexed substrings.
def slice_string(s):
    return s[1::2], s[0::2]
print(slice_string("hello"))