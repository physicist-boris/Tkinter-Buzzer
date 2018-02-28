from tkinter import tix
from tkinter import *



fenetre = tix.Tk()
fenetre.geometry("400x400")
liste_buzz = {}
liste_equipe = []


Label(fenetre, text="CRÉER EQUIPE").pack()

value = StringVar()
value.set("texte par défaut")
entree = Entry(fenetre, width=30)
entree.pack()


def dream():
    yupi = Tk()
    for i in liste_equipe:
        label = Label(yupi, text= i )
        label.pack()
    yupi.mainloop()

def add_equipe():
    liste_equipe.append(entree.get())
    entree.delete(0, END)

nope = 0
liste_nom_buzz = []

fruitSelect_var = []
def Affiche(evt):
    tuy = 0
    for i in fruitSelect_var:
        liste_buzz[tuy] = i.get()
        tuy += 1
def effacer_fenetre():
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
        fruitSelect_var.append((tix.StringVar()))
        listeFruits = tix.ComboBox(variable=fruitSelect_var[n], editable= True, dropdown=1,command = Affiche)
        listeFruits.entry.config(state='readonly')

        yop = 0
        for j in liste_equipe:
            listeFruits.insert(yop, j)
            yop+= 1

        listeFruits.pack()
        listeFruits.place(x= 100, y= a)
        a += 55
    bouton4 = Button(fenetre, text="Continuer", command=trois_fenetre)
    bouton4.pack()

def trois_fenetre():
    for c in fenetre.winfo_children():
        c.destroy()
    l = LabelFrame(fenetre, padx=45, pady=25)
    l.pack(fill="both", expand="yes")
    Label(l, text="EN ATTENTE DU BUZZ.....").pack()


    def on_key_press(event):
        dictop = [i for i in liste_buzz.keys()]
        if int(event.char) in dictop:

            for c in fenetre.winfo_children():
                c.destroy()
            Label(fenetre, text="PREMIER AU BUZZ ").pack()
            Label(fenetre, text=liste_buzz[int(event.char)]).pack()
            bouton5 = Button(fenetre, text="Continuer", command=trois_fenetre)
            bouton5.pack()

    fenetre.bind("<KeyPress>", on_key_press)


bouton1 = Button(fenetre, text="Ajouter équipe", command= add_equipe)
bouton1.pack()

bouton2 = Button(fenetre, text="Lister équipe", command= dream)
bouton2.pack()

bouton3 = Button(fenetre, text="Terminer", command = effacer_fenetre)
bouton3.pack()



fenetre.mainloop()

