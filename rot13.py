# -*- coding: UTF-8 -*-
import tkinter as tk

# fonction d'encodage
def encodage() :
    abc = 'abcdefghijklmnopqrstuvwxyz'
    message = texte_orig.get("1.0",tk.END)
    code = ''
    for car in message :
        if car in abc :
            for i in range(26) :
                if car == abc[i] :
                    code += abc[(i+13)%26]
        else :
            code += car
    texte_code.delete("1.0",tk.END) # on efface ce qu'il y avait écrit précédemment
    texte_code.insert(tk.END,code) # on colle le code complet

window = tk.Tk() # on crée la fenêtre

invite = tk.Label(master=window,text="Entrer le texte à coder :") # petite zone de texte
texte_orig = tk.Text(master=window,background="#34A2FE",height=5,wrap="word") # grande zone de texte éditable

texte_code = tk.Text(master=window,background="#FF968D",height=5,wrap="word")
btn_code = tk.Button(master=window,text="Coder le message",command=encodage) # la fonction encodage est appelée à chaque appui sur le bouton

# on dispose les différents éléments les uns en-dessous des autres
invite.pack(fill=tk.BOTH) # fill rend les cadres étirables
texte_orig.pack(expand=1,fill=tk.BOTH)
btn_code.pack(fill=tk.BOTH)
texte_code.pack(expand=1,fill=tk.BOTH)

window.mainloop() # lance la boucle des évènements qui enregistre toutes les interactions de l'utilisateurs avec l'appli
