# 27. Find roots of a quadratic equation
def quadratic_roots(a, b, c):
    d = (b ** 2) - (4 * a * c)
    if d < 0:
        return "Complex roots"
    root1 = (-b + d ** 0.5) / (2 * a)
    root2 = (-b - d ** 0.5) / (2 * a)
    return root1, root2

print("Roots of 2x^2 + 4x - 6:", quadratic_roots(2, 4, -6))