import time

list = []
c=0

start = time.perf_counter()
#===========================================#
for i in range(11111,66667):

    if "7" in str(i) or "8" in str(i) or "9" in str(i) or "0" in str(i):
        pass
    else:
        list.append(i)

for num in list:
    if "2" in str(num) and "5" in str(num):
        c=c+1

p = c/7776

print(f"{p:.3f}")
#===========================================#
end = time.perf_counter()

# Convert to milliseconds
elapsed_ms = (end - start) * 1000
print(f"Execution time: {elapsed_ms:.3f} ms")