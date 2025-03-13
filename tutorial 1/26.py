# 26. Find the distance between two points
def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print("Distance between (1,2) and (4,6):", distance(1, 2, 4, 6))