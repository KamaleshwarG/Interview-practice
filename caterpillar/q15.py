import math

def circle_intersection_area(x1, y1, r1, x2, y2, r2):
    # Calculate the distance between the centers of the circles
    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    # Check if the circles are completely separate
    if d >= r1 + r2:
        return 0.0  # No overlap, intersection area is 0

    # Check if one circle is completely inside the other
    elif d <= abs(r1 - r2):
        # Area of smaller circle is completely inside the larger circle
        return math.pi * min(r1, r2)**2

    else:
        # Calculate the area of intersection using the law of cosines
        A = (r1**2 * math.acos((d**2 + r1**2 - r2**2) / (2 * d * r1))
             + r2**2 * math.acos((d**2 + r2**2 - r1**2) / (2 * d * r2))
             - 0.5 * math.sqrt((-d + r1 + r2) * (d + r1 - r2) * (d - r1 + r2) * (d + r1 + r2)))

        return A

# Example usage
x1, y1, r1 = 0, 0, 3
x2, y2, r2 = 4, 0, 3
intersection_area = circle_intersection_area(x1, y1, r1, x2, y2, r2)
print(f"Area of intersection: {intersection_area}")
