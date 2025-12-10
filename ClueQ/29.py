from math import gcd
from collections import deque

fibonaccis = [102334155,165580141,267914296,433494437,701408733]
fibonaccis_formatdis = [[102 ,334, 155],[165, 580, 141],[267, 914, 296],[433, 494, 437],[701, 408, 733]]

cn1 = [267,851,259,433,493,165,701,102]
cn2 = [914,494,468,460,143,150,832,580,299,334,408]
cn3 = [296,763,155,23,168,437,733,154,141]

numdis = []
startingpoints = []
plist=[]
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



for i in range(0,720):
	numdis.append([cn1[i%8],cn2[i%11],cn3[i%9]])

for ele in fibonaccis_formatdis:
	startingpoints.append(numdis.index(ele))

for index in startingpoints:
	clicks = 0
	for i in numdis:
		display = (numdis[(index+numdis.index(i))%len(numdis)])
		d=deque(display)
		d2 = d.rotate(-1)
		d3 =d.rotate(-1)
		clicks = clicks + 2
		if listoftriples.count(display) == 1 or listoftriples.count(d2) == 1 or listoftriples.count(d3):
			p=clicks
			plist.append(p)
		
print(plist)
print(clicks)