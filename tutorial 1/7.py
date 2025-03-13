# 7. Find the quadrant of a point
x = float(input("Enter x coordinate: "))
y = float(input("Enter y coordinate: "))
if x > 0 and y > 0:
    print("Quadrant I")
elif x < 0 and y > 0:
    print("Quadrant II")
elif x < 0 and y < 0:
    print("Quadrant III")
elif x > 0 and y < 0:
    print("Quadrant IV")
else:
    print("On axis")
