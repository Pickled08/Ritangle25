cn1 = [1,2,3,4,5,6,7,8]
cn2 = [10,11,12,13,14,15,16,17,18,19,20]
cn3 = [1,2,3,4,5,6,7,8,9]

S=0
T=0

for i in range(792):
    n1=((i)%8)
    n2=((i)%11)
    n3=((i)%9)

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