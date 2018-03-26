from tkinter import Label
from tkinter import StringVar
from tkinter import Entry
from tkinter import Tk
from tkinter import LabelFrame
from tkinter import END
from tkinter import Button
from tkinter import tix
import tkinter.font as tkFont

"""
Code qui permet de créer des équipes et d'associer ces équipes à des touches du clavier("buzzers") et détermine
la premiere personne ayant appuyé sur le buzz
"""

main_window = tix.Tk()
main_window.geometry("400x400")
dict_buzz = {}
liste_equipe = []
equipe_select_var = []

Label(main_window, text="CRÉER EQUIPE").pack()


color_font_entry = tkFont.Font(slant ='italic')
value = StringVar()
entree = Entry(main_window, textvariable = value,  width=30, font = color_font_entry, bg = "yellow")
entree.pack()



def affiche_equipe():
    """
    Fonction qui crée une nouvelle fenêtre avec la liste des différents équipes du jeu
    :return:
    """
    liste_equipe_affiche = Tk()
    for i in liste_equipe:
        label = Label(liste_equipe_affiche, text= i )
        label.pack()
    liste_equipe_affiche.mainloop()


def modifier_equipe():
    pass




def add_equipe():
    """
    Fonction qui permet d'ajouter des équipes à la liste des équipes(liste_equipe) avec le bouton "Ajouter équipe"
    :return:
    """
    equipe = entree.get().strip()
    print(equipe)
    if len(list(equipe)) >= 1:
        if (equipe.lower() in liste_equipe) is not True:
            liste_equipe.append(equipe.lower())
            entree.delete(0, END)



def addition_team(event):
    """
    Fonction qui permet d'ajouter des équipes à la liste des équipes(liste_equipe) avec la touche "entrée"
    :param event:
    :return:
    """
    equipe = entree.get().strip()
    print(equipe)
    if len(list(equipe)) >= 1:
        if (equipe.lower() in liste_equipe) is not True:
            liste_equipe.append(equipe.lower())
            entree.delete(0, END)



def buzz_association(evt):
    """
    Fonction qui pour chaque clés du dictionnaire liste_buzz(0, 1,2...) associe une valeur
    sous forme de chaîne de caractère correspondant à une équipe
    :param evt:
    :return:
    """
    indice_dict = 0
    for i in equipe_select_var:
        dict_buzz[indice_dict] = i.get()
        indice_dict += 1


def window_buzz_association():
    """
    deuxième fenetre où se déroule l'association des équipes à un buzzer
    :return:
    """
    for c in main_window.winfo_children():
        c.destroy()
    label_frame = LabelFrame(main_window, padx=35, pady=15)
    label_frame.pack(fill="both", expand="yes")

    Label(label_frame, text="LIER ÉQUIPE").pack()
    Label(main_window, text ="Buzzers").pack()
    a = 90

    for n in range(0, (len(liste_equipe))):
        nom_buzz = "Buzz0{}".format(str(n))
        Label(main_window, text= nom_buzz).place(x = 45, y= a)
        equipe_select_var.append((tix.StringVar()))
        selection_equipe = tix.ComboBox(variable=equipe_select_var[n], editable= True, dropdown=1, command = buzz_association)
        selection_equipe.entry.config(state='readonly', bg = "red")

        i = 0
        for j in liste_equipe:
            selection_equipe.insert(i, j)
            i+= 1

        selection_equipe.pack()
        selection_equipe.place(x= 100, y= a)
        a += 55
    btn_liste_equipe = Button(main_window, text="Lister équipe", command=affiche_equipe)
    btn_liste_equipe.pack()
    btn_modify_team = Button(main_window, text="Modifier équipe", command=modifier_equipe)
    btn_modify_team.pack()
    btn_continuer= Button(main_window, text="Continuer", command=window_declare_winner)
    btn_continuer.pack()



def window_declare_winner():
    """
    derniere fenetre qui vérifie constamment si un joueur a appuyé sur une touche et désigne le gagnant
    :return:
    """
    for c in main_window.winfo_children():
        c.destroy()
    label_frame = LabelFrame(main_window, padx=45, pady=25)
    label_frame.pack(fill="both", expand="yes")
    Label(label_frame, text="EN ATTENTE DU BUZZ.....").pack()


    def on_key_press(event):
        """
        fonction callback qui agit  suite à une touche appuyé et qui affiche l'équipe premier au buzz
        :param event:
        :return:
        """
        main_window.unbind("<KeyPress>")
        dictop = [i for i in dict_buzz.keys()]
        try:
            if int(event.char) in dictop:

                    for c in main_window.winfo_children():
                        c.destroy()
                    Label(main_window, text="PREMIER AU BUZZ ").pack()
                    Label(main_window, text=dict_buzz[int(event.char)]).pack()

                    btn_continuer = Button(main_window, text="Continuer", command=window_declare_winner)
                    btn_continuer.pack()
                    btn_liste_equipe = Button(main_window, text="Lister équipe", command=affiche_equipe)
                    btn_liste_equipe.pack()
            else:
                window_declare_winner()
        except:
            window_declare_winner()

    main_window.bind("<KeyPress>", on_key_press)



btn_ajouter_equipe = Button(main_window, text="Ajouter équipe", command= add_equipe)
btn_ajouter_equipe.pack()

main_window.bind("<Return>", addition_team)

btn_liste_equipe = Button(main_window, text="Lister équipe", command= affiche_equipe)
btn_liste_equipe.pack()

btn_terminer = Button(main_window, text="Terminer", command = window_buzz_association)
btn_terminer.pack()





main_window.mainloop()
