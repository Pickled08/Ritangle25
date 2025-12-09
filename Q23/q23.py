from itertools import permutations

word=["D","O","D","E","C","A","H","E","D","R","O","N"]

permutations=set(permutations(word))

for perm in permutations:
    print(perm)