from itertools import combinations
import math

h=[]

nums = list(range(1, 11))

splits = []
seen = set()

for combo in combinations(nums, 5):
    left = list(combo)
    right = [x for x in nums if x not in left]

    signature = (tuple(sorted(left)), tuple(sorted(right)))

    if signature not in seen:
        seen.add(signature)
        splits.append((left, right))

for a, b in splits:
    aP =math.prod(a)
    bP =math.prod(b)
    hcf = math.gcd(aP, bP)
    h.append(hcf)

h=set(h)
print(sum(h))