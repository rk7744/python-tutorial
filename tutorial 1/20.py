# 20. Check if a string is a palindrome using slicing
def is_palindrome(s):
    return s == s[::-1]
print("Is 'racecar' a palindrome?", is_palindrome("racecar"))