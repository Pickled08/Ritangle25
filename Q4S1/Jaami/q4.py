from itertools import permutations

side1 = 75 #side0
side2 = 75 #side1
side3 = 135 #side2
side4 = 135 #side3
side5 = 405 #side4
side6 = 405 #side5

options = [0, 1, 2, 3, 4, 5]

for perm in permutations(options):
    val1 = side1 * perm[0]
    val2 = side2 * perm[1]
    val3 = side3 * perm[2]
    val4 = side4 * perm[3]
    val5 = side5 * perm[4]
    val6 = side6 * perm[5]
    total = val1 + val2 + val3 + val4 + val5 + val6
    if total == 2025:
        for i in range(6):
            print(f"Side {i + 1} is assigned: ", perm[i])
        break