fibonaccis = [102334155,165580141,267914296,433494437,701408733]
fibonaccis_formatdis = [[102 ,334, 155],[165, 580, 141],[267, 914, 296],[433, 494, 437],[701, 408, 733]]

cn1 = [267,851,259,433,493,165,701,102]
cn2 = [914,494,468,460,143,150,832,580,299,334,408]
cn3 = [296,763,155,23,168,437,733,154,141]

numdis = []
startingpoints = []

for i in range(0,720):
	numdis.append([cn1[i%8],cn2[i%11],cn3[i%9]])

for ele in fibonaccis_formatdis:
	startingpoints.append(numdis.index(ele))

for index in startingpoints:
	clicks = 0
	for i in range(0,720):
		display = (numdis[(index+1)%len(numdis)])
		clicks = clicks + 2
		

print(clicks)