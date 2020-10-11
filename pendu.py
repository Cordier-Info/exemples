from dessins_pendu import *
import getpass

nb_erreur, tour = 0 , 0
mot = getpass.getpass().upper()
print()
mot_partiel = list('_' * (len(mot)))
print("Mot mystère : " + ' '.join(mot_partiel))

while "_" in mot_partiel:
    print("\n"+"#"*10,"Tour",tour,"#"*10)
    lettre = input("\nChosir une lettre : ").upper()
    if lettre in mot:
        print("\nBon choix !\n")
        for i, l in enumerate(mot):
            if l == lettre:
                mot_partiel[i] = lettre
    else:
        nb_erreur += 1
        print("\nRaté !")
        print(dessin[nb_erreur])
        if nb_erreur == 7:
            print(">>> G A M E  O V E R <<<\n")
            break
    print("Mot mystère : " + ' '.join(mot_partiel))
    tour += 1

else:
    print("\n\n>>> B R A V O ! <<<\n")
