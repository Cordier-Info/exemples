def moyennes(liste) :
        sa,sg,invsh = 0,1,0
        n = len(liste)
        for i in liste :
            sa += i
            sg *= i
            invsh += 1/i
        ma = sa/n
        mg = sg**(1/n)
        mh = n/invsh
        return ma,mg,mh
        
print(moyennes([10,1000]))
notes = [10,15,8,12,18,6]
moy = moyennes(notes)[0]
print('La moyenne des notes est de', moy)
