# 9. Reverse the first and second half of a string separately.
def reverse_halves(s):
    mid = len(s) // 2
    return s[:mid][::-1] + s[mid:][::-1]
print(reverse_halves("abcdefgh"))