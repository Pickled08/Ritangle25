from math import gcd
import math

fibonaccis = [102334155, 165580141, 267914296, 433494437, 701408733]
fibonaccis_formatdis = [
    [102, 334, 155],
    [165, 580, 141],
    [267, 914, 296],
    [433, 494, 437],
    [701, 408, 733],
]

cn1 = [267, 851, 259, 433, 493, 165, 701, 102]
cn2 = [914, 494, 468, 460, 143, 150, 832, 580, 299, 334, 408]
cn3 = [296, 763, 155, 145, 168, 437, 733, 154, 141]

numdis = []
startingpoints = []
plist = []
qlist = []
rlist = []
slist = []


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


def genTriples(k):
    n, m = 1, 2
    while m * m + 1 < k:  # while z<k (for largest m producing z)
        if n >= m:
            n, m = m % 2, m + 1  # n reached m, advance m, reset n
        z = m * m + n * n  # compute z
        if z >= k:
            n = m
            continue  # skip remaining n when z >= k
        if gcd(n, m) == 1:  # trigger on coprimes
            yield m * m - n * n, 2 * m * n, z  # return x,y,z triple
        n += 2  # advance n, odds with evens


listoftriples = []

for x, y, z in genTriples(1000):
    listoftriples.append([x, y, z])


for i in range(0, 720):
    numdis.append([cn1[i % 8], cn2[i % 11], cn3[i % 9]])

for ele in fibonaccis_formatdis:
    startingpoints.append(numdis.index(ele))

for index in startingpoints:
    clicks = 0
    p = 0
    q = 0
    r = 0
    s=0
    for i in numdis:
        display = numdis[(index + numdis.index(i)) % len(numdis)]
        if p == 0:
            if (
                (display[0] ** 2 + display[1] ** 2 == display[2] ** 2)
                or (display[1] ** 2 + display[2] ** 2 == display[0] ** 2)
                or (display[2] ** 2 + display[0] ** 2 == display[1] ** 2)
            ):
                if gcd(display[0], display[1], display[2]) == 1:
                    p = clicks
                    plist.append(p)

        if q == 0 and p != 0:
            if any(
                x == 60 for x in get_triangle_angles(display[0], display[1], display[2])
            ):
                q = clicks - p
                qlist.append(q)

        if r == 0 and p != 0 and q != 0:
            a, b, c = display[:3]
            S = (a + b + c) / 2
            expr = S * (S - a) * (S - b) * (S - c)

            if expr >= 0:
                area = math.sqrt(expr)
                if round(area, 5).is_integer():
                    r = clicks - p - q
                    rlist.append(r)
            else:
                continue
        if s==0 and r!=0 and p!=0 and q!=0:
            string_num = str(display[0]) + str(display[1]) + str(display[2])
            if string_num in ["102334155", "165580141", "267914296", "433494437", "701408733"]:
                s=clicks -p -q -r
                slist.append(s)
            

        clicks = clicks + 2

products = []

for i in range(len(plist)):
    p = plist[i]
    q = qlist[i]
    r = rlist[i]
    s = slist[i]
    product = p * q * r * s
    products.append(product)

print(max(products))
