import itertools

c=0

dicenum = [1,2,3,4,5,6]

# Length of combinations you want (e.g., length 2)
combination_length = 3

# Generate the combinations
all_combinations = itertools.product(dicenum, repeat=combination_length)

# Convert the iterator to a list of tuples for display
combinations_list = list(all_combinations)

for elm in combinations_list:
    p=elm[0]
    q=elm[1]
    r=elm[2]

    #is triangle obtuses
    if p>(q+r) or q>(p+r) or r>(p+q):
        c+=1

print(len(combinations_list))
print(c)

print(c/len(combinations_list))