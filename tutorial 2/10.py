# 10. Validate password based on given criteria.
import re
def validate_password(pwd):
    if (len(pwd) >= 6 and re.search(r'[a-z]', pwd) and re.search(r'[A-Z]', pwd) and
        re.search(r'[0-9]', pwd) and re.search(r'[#$@]', pwd)):
        return True
    return False

print(validate_password("Abc#123"))