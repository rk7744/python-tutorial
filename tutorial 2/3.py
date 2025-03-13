# 3. Palindrome check without reversing the string.
def is_palindrome(s):
    return all(s[i] == s[-i - 1] for i in range(len(s) // 2))
print(is_palindrome("madam"))