from tkinter import tix
from tkinter import *



fenetre = tix.Tk()   #creation d'une interface principale où se déroule tous les évènements(actions)
fenetre.geometry("400x400")#taille de la fenêtre
liste_buzz = {}#dictionnaire qui à chaque clé(0, 1, 2,...) associe une équipe choisis par l'utilisateur. Exemple: {0: "Togo", 1: "Sénégal"}
liste_equipe = []#liste qui contient toutes les différentes équipes qui ont été entrées au début de jeu
equipe_Select_var = []#disons que c'est une liste qui contient tous les différentes variable des "Combobox" parce que à chaque combobox est associé une variable
                        #qui correspondant à la variable sélectionnée dans une liste de choix

Label(fenetre, text="CRÉER EQUIPE").pack()

value = StringVar()
value.set("texte par défaut")
entree = Entry(fenetre, width=30)
entree.pack()


#Fonction qui crée une nouvelle fenêtre avec la liste des différents équipes du jeu
def Affiche_equipe():
    liste_equipe_affiche = Tk()
    for i in liste_equipe:
        label = Label(liste_equipe_affiche, text= i )
        label.pack()
    liste_equipe_affiche.mainloop()


def Modifier_equipe():
    pass



#Fonction(ou commande) qui permet d'ajouter des équipes à la liste des équipes(liste_equipe) avec le bouton "Ajouter équipe"
def add_equipe():
    if len(list(entree.get())) >= 1:
        if (entree.get().lower() in liste_equipe) is not True:
            print(entree.get())
            liste_equipe.append(entree.get().lower())
            entree.delete(0, END)


#Fonction(ou commande) qui permet d'ajouter des équipes à la liste des équipes(liste_equipe) avec la touche entrée
def addition_team(event):
    if len(list(entree.get())) >= 1:
        if (entree.get().lower() in liste_equipe) is not True:
            liste_equipe.append(entree.get().lower())
            entree.delete(0, END)


#Fonction(ou commande) qui pour chaque clés du dictionnaire liste_buzz(0, 1,2...) associe une valeur sous forme de chaîne de caractère correspondant à une équipe
def Association_de_buzz(evt):
    tuy = 0
    for i in equipe_Select_var:
        liste_buzz[tuy] = i.get()
        tuy += 1

#deuxième fenetre où se déroule l'association des équipes à un buzzer
def deuxieme_fenetre():
    for c in fenetre.winfo_children():
        c.destroy()
    l = LabelFrame(fenetre, padx=35, pady=15)
    l.pack(fill="both", expand="yes")

    Label(l, text="LIER ÉQUIPE").pack()
    Label(fenetre, text = "Buzzers").pack()
    a = 90

    for n in range(0, (len(liste_equipe))):
        nom_buzz = "Buzz0{}".format(str(n))
        Label(fenetre, text= nom_buzz).place(x = 45, y= a)
        equipe_Select_var.append((tix.StringVar()))
        Selection_equipe = tix.ComboBox(variable=equipe_Select_var[n], editable= True, dropdown=1,command = Association_de_buzz)
        Selection_equipe.entry.config(state='readonly')

        yop = 0
        for j in liste_equipe:
            Selection_equipe.insert(yop, j)
            yop+= 1

        Selection_equipe.pack()
        Selection_equipe.place(x= 100, y= a)
        a += 55
    bouton6 = Button(fenetre, text="Lister équipe", command=Affiche_equipe)
    bouton6.pack()
    bouton8 = Button(fenetre, text="Modifier équipe", command=Modifier_equipe)
    bouton8.pack()
    bouton4 = Button(fenetre, text="Continuer", command=troisieme_fenetre)
    bouton4.pack()


#derniere fenetre qui vérifie constamment si un joueur a appuyé sur une touche et désigne le gagnant
def troisieme_fenetre():
    for c in fenetre.winfo_children():
        c.destroy()
    l = LabelFrame(fenetre, padx=45, pady=25)
    l.pack(fill="both", expand="yes")
    Label(l, text="EN ATTENTE DU BUZZ.....").pack()

    #fonction qui "agit" suite à une touche appuyé et qui affiche l'équipe premier au buzz
    def on_key_press(event):
        fenetre.unbind("<KeyPress>")
        dictop = [i for i in liste_buzz.keys()]
        if int(event.char) in dictop:

            for c in fenetre.winfo_children():
                c.destroy()
            Label(fenetre, text="PREMIER AU BUZZ ").pack()
            Label(fenetre, text=liste_buzz[int(event.char)]).pack()

            bouton5 = Button(fenetre, text="Continuer", command=troisieme_fenetre)
            bouton5.pack()
            bouton7 = Button(fenetre, text="Lister équipe", command=Affiche_equipe)
            bouton7.pack()

    fenetre.bind("<KeyPress>", on_key_press)



bouton1 = Button(fenetre, text="Ajouter équipe", command= add_equipe)
bouton1.pack()

fenetre.bind("<Return>", addition_team)

bouton2 = Button(fenetre, text="Lister équipe", command= Affiche_equipe)
bouton2.pack()

bouton3 = Button(fenetre, text="Terminer", command = deuxieme_fenetre)
bouton3.pack()



fenetre.mainloop()
