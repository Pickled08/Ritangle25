import time

cn1 = [267,851,259,433,493,165,7,102]
cn2 = [494,468,460,143,150,832,580,299,334,19]
cn3 = [20,21,22,23,24,25,26,27,28]

S=0
T=0

start = time.perf_counter()

for i in range(792):
    n1=((i)%len(cn1))
    n2=((i)%len(cn2))
    n3=((i)%len(cn3))

    t = 1000*cn1[n1] + 10*cn2[n2] + cn3[n3]

    S = S + t

print(S)

for i in range(792):
    n1=((i)%8)
    n2=((i)%11)
    n3=((i)%9)

    t = cn1[n1] * cn2[n2] * cn3[n3]

    T = T + t

print(T)

print(S/T)

end = time.perf_counter()

# Convert to milliseconds
elapsed_ms = (end - start) * 1000
print(f"Execution time: {elapsed_ms:.3f} ms")