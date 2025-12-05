from itertools import permutations

num=[2,3,4,5,6,7]

Dlist = []

permutations=set(permutations(num))

for perm in permutations:
    ru=((perm[2])/perm[0])**(1/(perm[1]-1))
    if ru < 1 and ru > 0:
        rv=((perm[5])/perm[3])**(1/(perm[4]-1))
        if rv < 1 and rv > 0:
            D=abs(((perm[0])/(1-ru))-((perm[3])/(1-rv)))

            Dlist.append(D)

print(max(Dlist))


#ru=((4)/6)**(1/(3-1))
#if ru < 1 and ru > 0:
#    rv=((5)/7)**(1/(2-1))
#    if rv < 1 and rv > 0:
#        D=abs(((6)/(1-ru))-((7)/(1-rv)))
#
#        print(D)
#        print(ru)
#        print(rv)