total = 0
Max = 50

for a in range(Max):
    for b in range(Max):
        for c in range(Max):
            for d in range(Max):
                term = (2**a) * (3**b) * (5**c) * (7**d)
                total += 1/term

print(f"Total sum: {total}")