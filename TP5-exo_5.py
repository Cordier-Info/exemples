fi = open('samedi.txt','r')
texte = fi.read()
fi.close()
paras = []
# On sépare d'abord le texte en paragraphe
# puis on récupère chaque mot (.strip() permet d'enlever les espaces)
for para in texte.split('\n'):
    mots = []
    for mot in para.strip().split():
        mots.append(mot) # liste de tous les mots
    paras.append(' '.join(mots)) # on regroupe les mots en paragraphes
texte_censuré = '\n'.join(paras) # on regroupe les paragraphes pour reformer le texte complet
fo = open('samedi_censure.txt','w')
print(texte_censuré,file = fo)
