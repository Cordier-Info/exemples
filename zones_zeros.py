import numpy as np
from scipy import ndimage

M = np.array([0,0,0,1,1,1,1,0,0,1,1,0,1,1,0,1,1,0,0,0])
M.shape = (4,5)

print(M,'\n')
def zones_zeros(M) :
    """
    argument M : tableau 2D de 1 et 0
    retourne autant de tableaux 2D qu'il y de zones contiguës de 0 dans M.
    Chaque tableau est une copie de M où seule une des zones de 0 contigus est présente (le reste est rempli de 1).
    """
    M_zones, nb_zones =  ndimage.label(M==0)
    print("Il y {} zones de zéros contigus repérées\n{}\n".format(nb_zones,M_zones))
    T = []
    for i in range(1,nb_zones+1) :
        T.append(np.where(M_zones==i,0,1))
    return T

for i,tab in enumerate(zones_zeros(M)) :
    print("zone {} :\n{}".format(i+1,tab))
