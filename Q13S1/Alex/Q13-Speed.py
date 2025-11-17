import time

from itertools import permutations

start = time.perf_counter()
#===========================================#

l1=[1,0,0,0,0,0]
l2=[1,1,0,0,0,0]
l3=[1,1,1,0,0,0]
l4=[1,1,1,1,0,0]
l5=[1,1,1,1,1,0]

permutations1=set(permutations(l1))
permutations2=set(permutations(l2))
permutations3=set(permutations(l3))
permutations4=set(permutations(l4))
permutations5=set(permutations(l5))

permutations=(len(permutations1)+len(permutations2)+len(permutations3)+len(permutations4)+len(permutations5))*9**3

print(permutations)

#===========================================#
end = time.perf_counter()

# Convert to milliseconds
elapsed_ms = (end - start) * 1000
print(f"Execution time: {elapsed_ms:.3f} ms")