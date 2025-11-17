import time


start = time.perf_counter()
#===========================================#

count = 0

for h in range(0,100):
    for m in range(0,60):
        for s in range(0,60):
            h=str(h).zfill(2)
            m=str(m).zfill(2)
            s=str(s).zfill(2)
            hhmmss = h+m+s

            c1=int(bool(hhmmss.count("1")))
            c2=int(bool(hhmmss.count("2")))
            c3=int(bool(hhmmss.count("3")))
            c4=int(bool(hhmmss.count("4")))
            c5=int(bool(hhmmss.count("5")))
            c6=int(bool(hhmmss.count("6")))
            c7=int(bool(hhmmss.count("7")))
            c8=int(bool(hhmmss.count("8")))
            c9=int(bool(hhmmss.count("9")))
            c0=int(bool(hhmmss.count("0")))
            
            sum = c1+c2+c3+c4+c5+c6+c7+c8+c9+c0

            if sum == 2:
                count = count + 1
                print(hhmmss)


print(count)

#===========================================#
end = time.perf_counter()

# Convert to milliseconds
elapsed_ms = (end - start) * 1000
print(f"Execution time: {elapsed_ms:.3f} ms")