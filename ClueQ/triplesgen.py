from math import gcd

def genTriples(k):
    n,m = 1,2
    while m*m+1<k:                  # while z<k (for largest m producing z)
        if n>=m: n,m = m%2,m+1      # n reached m, advance m, reset n
        z = m*m+n*n                 # compute z 
        if z >= k: n=m;continue     # skip remaining n when z >= k
        if gcd(n,m) == 1:           # trigger on coprimes
            yield m*m-n*n,2*m*n,z   # return x,y,z triple
        n += 2                      # advance n, odds with evens

listoftriples = []

for x,y,z in genTriples(1000):
    listoftriples.append([x,y,z])

