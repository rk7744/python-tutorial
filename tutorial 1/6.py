# 6. Check for right-angled triangle
x, y, z = map(int, input("Enter three sides: ").split())
if x**2 + y**2 == z**2 or x**2 + z**2 == y**2 or y**2 + z**2 == x**2:
    print("Right-angled triangle")
else:
    print("Not a right-angled triangle")
