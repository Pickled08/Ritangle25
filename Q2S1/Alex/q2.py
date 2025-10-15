from itertools import permutations
import time

word = ["R","I","T","A","N","G","L","E"]

alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def distance(len_my_list, idx_1, idx_2):
    i = (idx_1 - idx_2) % len_my_list
    j = (idx_2 - idx_1) % len_my_list
    return min(i, j)

start = time.perf_counter()
#===========================================#

pathlens = []

permutations=set(permutations(word))

for perm in permutations:
    D=0
    for p in range(8 - 1):
        d=distance(len(alphabet), alphabet.index(perm[p]), alphabet.index(perm[p+1]))
        D = D + d

    pathlens.append(D)

x=min(pathlens)
y=max(pathlens)  
print("x (Min)=")
print(min)
print("y (Max)=")
print(max)

xy=x*y

print("x*y=")
print(xy)

#===========================================#
end = time.perf_counter()

# Convert to milliseconds
elapsed_ms = (end - start) * 1000
print(f"Execution time: {elapsed_ms:.3f} ms")
