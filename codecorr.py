import numpy as np

n = 9
k = 3
mots = []

# matrice génératrice
G = np.array([[1,1,0,1,1,0,1,0,0],
                [0,1,0,0,0,1,1,1,1],
                [1,0,1,0,0,0,1,1,1]])
print("G =")
print(G)
print()

# liste des mots codes :
print("Liste des mots codes :")
for i in range(2**k) :
    u = [int('{0:0{1}b}'.format(i,k)[j]) for j in range(k)]
    m = np.dot(u,G)
    m %= 2
    mots.append(m)
    print(m)
print()

# on met G sous forme échelonnée
G[0] += G[1]
G[2] += G[0]
G %= 2
print("Gech =")
print(G)
print()

# on isole le bloc P
P = G[:,3:]
print("P =")
print(P)
print()

# on en déduit la matrice de parité H
Pt = P.transpose()
H = np.concatenate((Pt, np.identity(6)), axis=1).astype(np.uint8)
print("H =")
print(H)
print()

# on imprime les syndromes et les éléments de la classe correspondante
print("syndromes et classes associées (une erreur) :")
for i in range(n) :
    e = np.zeros(n)
    e[i] = 1
    s = np.dot(e,H.transpose())%2
    print("s{} = ".format(i),s.astype(np.uint8))
    for m in mots :
        print(((m+e)%2).astype(np.uint8), end=' ')
    print()

print()
print("syndromes et classes associées (deux erreurs dont une en première position) :")
for i in range(1,n) :
    e = np.zeros(n)
    e[0] = 1
    e[i] = 1
    s = np.dot(e,H.transpose())%2
    print("s{} = ".format(i),s.astype(np.uint8))
    for m in mots :
        print(((m+e)%2).astype(np.uint8), end=' ')
    print()
