# 22. Check if a year is a leap year
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
print("Is 2024 a leap year?", is_leap_year(2024))