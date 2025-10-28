import time

start = time.perf_counter()
#===========================================#
count = 0
for a in range(1,7):
    for b in range(1,7):
        for c in range(1,7):
            for d in range(1,7):
                for e in range(1,7):
                    if (a == 2 or b == 2 or c == 2 or d == 2 or e == 2) and (a == 5 or b == 5 or c == 5 or d == 5 or e == 5):
                        count += 1

print(count/7776)
#===========================================#
end = time.perf_counter()

# Convert to milliseconds
elapsed_ms = (end - start) * 1000
print(f"Execution time: {elapsed_ms:.3f} ms")