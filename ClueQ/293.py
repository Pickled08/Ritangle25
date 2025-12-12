from math import gcd, acos, degrees, sqrt
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
    if not (a + b > c and a + c > b and b + c > a and a > 0 and b > 0 and c > 0):
        return None 

    cos_A = (b**2 + c**2 - a**2) / (2 * b * c)
    cos_B = (a**2 + c**2 - b**2) / (2 * a * c)
    cos_C = (a**2 + b**2 - c**2) / (2 * a * b)

    cos_A = max(-1.0, min(1.0, cos_A))
    cos_B = max(-1.0, min(1.0, cos_B))
    cos_C = max(-1.0, min(1.0, cos_C))

    angle_A = degrees(acos(cos_A))
    angle_B = degrees(acos(cos_B))
    angle_C = degrees(acos(cos_C))

    return round(angle_A, 6), round(angle_B, 6), round(angle_C, 6)


for i in range(0, 792):
    numdis.append([cn1[i % len(cn1)], cn2[i % len(cn2)], cn3[i % len(cn3)]])

for ele in fibonaccis_formatdis:
    try:
        startingpoints.append(numdis.index(ele))
    except ValueError:
        raise RuntimeError(f"Starting triple {ele} not found in generated displays")

for index in startingpoints:
    clicks = 0
    p = q = r = s = None

    for i in range(0, 792):
        display = numdis[(index + i) % 792]
        a, b, c = display

        if p is None:
            if (a*a + b*b == c*c) or (b*b + c*c == a*a) or (c*c + a*a == b*b):
                if gcd(gcd(a, b), c) == 1:
                    p = clicks

        if p is not None and q is None:
            angles = get_triangle_angles(a, b, c)
            if angles is not None and any(abs(x - 60.0) < 1e-6 for x in angles):
                q = clicks - p

        if p is not None and q is not None and r is None:
            S = (a + b + c) / 2.0
            expr = S * (S - a) * (S - b) * (S - c)
            if expr >= 0:
                area = sqrt(expr)
                if abs(area - round(area)) < 1e-6:
                    r = clicks - p - q

        if p is not None and q is not None and r is not None and s is None:
            string_num = f"{a}{b}{c}"
            if string_num in [str(x) for x in fibonaccis]:
                s = clicks - p - q - r
                break

        clicks += 2

    if any(x is None for x in (p, q, r, s)):
        raise RuntimeError(f"Could not find all p,q,r,s for start index {index}")
    plist.append(p)
    qlist.append(q)
    rlist.append(r)
    slist.append(s)

products = [plist[i] * qlist[i] * rlist[i] * slist[i] for i in range(len(plist))]
print("min product =", min(products))
