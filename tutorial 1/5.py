# 5. Roots of a quadratic equation
import cmath
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
d = (b**2) - (4*a*c)
root1 = (-b + cmath.sqrt(d)) / (2 * a)
root2 = (-b - cmath.sqrt(d)) / (2 * a)
print("Roots:", root1, "and", root2)
