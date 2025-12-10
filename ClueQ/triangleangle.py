import math


def get_triangle_angles(a, b, c):
    # Triangle Inequality Theorem: Sum of any two sides > third side
    if not (a + b > c and a + c > b and b + c > a and a > 0 and b > 0 and c > 0):
        return "Invalid sides: These lengths cannot form a triangle."

    # Law of Cosines to find angles (results in radians)
    # Angle A (opposite side a)
    cos_A = (b**2 + c**2 - a**2) / (2 * b * c)
    # Angle B (opposite side b)
    cos_B = (a**2 + c**2 - b**2) / (2 * a * c)
    # Angle C (opposite side c)
    cos_C = (a**2 + b**2 - c**2) / (2 * a * b)

    # Convert radians to degrees
    angle_A = math.degrees(math.acos(cos_A))
    angle_B = math.degrees(math.acos(cos_B))
    angle_C = math.degrees(math.acos(cos_C))

    return round(angle_A, 5), round(angle_B, 5), round(angle_C, 5)


print(type(get_triangle_angles(851, 494, 763)))
