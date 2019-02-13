import tkinter as tk
from tkinter import Button
from tkinter import StringVar
from tkinter import Entry
import tkinter.font as tkFont
from tkinter import END
from tkinter import OptionMenu
from tkinter import Checkbutton
from tkinter import BooleanVar
from tkinter import Toplevel


class Window_General_Function(tk.Tk):
    """
    Cette classe permet d'initialiser la première fenêtre et contient les méthodes générales utilisées par les autres autres classes
    """

    def __init__(self):
        """
        self.container : une frame sur laquelle sont stockées les autres frames(différentes fenêtres).
        """
        tk.Tk.__init__(self)
        self.list_team = []
        self.list_frame = []
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        self.geometry("600x600")
        self.color_font_entry = tkFont.Font(slant='italic')
        for F in (Menu_Create_Team, Window_Association_Buzzer, Window_Detect_Winner, Window_Show_Winner):
            self.list_frame.append(F)

        # je commence par invoquer la première fenêtre
        self.switch_frame(self.container, "Menu_Create_Team", controller=self)

    def switch_frame(self, container, window_name, controller):
        """
        Fonction qui permet de changer de fênetre(frame)

        :param container:

        :param window_name:

        :param controller:représente une instance de classe que j'appellerai dans une autre classe dans le but d'hériter de certains
        attributs présents dans le __init__ d'une autre classe

        :return:
        """
        for frame in self.list_frame:
            if window_name == frame.__name__:
                if window_name == "Window_Detect_Winner":
                    liste_keys = [i.get() for i in controller.list_variable_team.values()]
                    if len(liste_keys) != len(set(liste_keys)):
                        return
                    else:
                        frame_to_call = frame(container, controller)
                        frame_to_call.grid(row=0, column=0, sticky="nsew")
                        frame_to_call.tkraise()
                else:
                    frame_to_call = frame(container, controller)
                    frame_to_call.grid(row=0, column=0, sticky="nsew")
                    frame_to_call.tkraise()

    def add_equipe(self):
        """
        Fonction qui permet d'ajouter des équipes à la liste des équipes(liste_equipe) avec le bouton "Ajouter équipe"
        :return:
        """
        team = self.entree.get().strip()
        if len(list(team)) >= 1:
            if (team.lower() in self.list_team) is not True:
                self.list_team.append(team.lower())
                self.entree.delete(0, END)

    def show_team(self):
        """
        Fonction qui crée une nouvelle fenêtre avec la liste des différents équipes du jeu
        :return:
        """
        list_team_showing = tk.Tk()
        for i in self.list_team:
            label = tk.Label(list_team_showing, text=i)
            label.pack()
        list_team_showing.mainloop()



    def add_key(self):
        self.dict_key = {}
        self.n = 0
        self.add_key = Toplevel(self.Obj_Window_General_Function)
        self.add_key.geometry("500x100")
        label = tk.Label(self.add_key, text = "Appuie sur des touches du clavier pour choisir lesquelles seront liées au buzzer")
        label.pack()
        self.add_key.focus_set()
        self.add_key.bind("<KeyPress>", self.on_key_add)
        self.add_key.protocol("WM_DELETE_WINDOW", self.on_closing_add_key)
    def on_key_add(self, event):
        self.dict_key[self.n] = event.char
        self.n += 1

    def on_closing_add_key(self):
        self.add_key.unbind("<KeyPress>")
        self.add_key.destroy()



    def erase_team(self):
        """
        Fonction qui crée une nouvelle fenêtre dans laquelle on peut effacer des équipes. bouton("Effacer une équipe")
        :return:
        """
        self.list_team_to_erase = Toplevel(self.Obj_Window_General_Function)
        label = tk.Label(self.list_team_to_erase, text="Sélectionner une équipe à effacer et fermer la fenêtre")
        label.pack()
        self.dict_check_button_team = {}
        for i in self.list_team:
            var = BooleanVar(self)
            self.dict_check_button_team[i] = var
            chk = Checkbutton(self.list_team_to_erase, text=i, variable=var)
            chk.pack()

        self.list_team_to_erase.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.list_team_to_erase.mainloop()

    def on_closing(self):
        """
        fonction qui s'éxcute lorsqu'on ferme la fenêtre "erase_team"
        :return:
        """
        for chk in self.dict_check_button_team.keys():
            if self.dict_check_button_team[chk].get() == True:
                self.list_team.remove(chk)
            else:
                pass
        self.list_team_to_erase.destroy()




class Menu_Create_Team(tk.Frame, Window_General_Function):
    """
    Classe associée à la fenêtre (frame) où l'on crée les équipes
    """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.Obj_Window_General_Function = controller
        self.container = controller.container
        self.list_team = controller.list_team
        self.dict_key = {}
        self.list_frame = controller.list_frame
        self.color_font_entry = controller.color_font_entry
        tk.Label(self, text="CRÉER EQUIPE").pack()
        self.value = StringVar()
        self.entree = Entry(self, textvariable=self.value, width=30, font=controller.color_font_entry, bg="yellow")
        self.entree.pack()
        btn_ajouter_equipe = Button(self, text="Ajouter une équipe", command=self.add_equipe)
        btn_ajouter_equipe.pack()
        btn_liste_equipe = Button(self, text="Liste des équipes", command=self.show_team)
        btn_liste_equipe.pack()
        btn_terminer = Button(self, text="Continuer",
                              command=lambda: self.switch_frame(self.container, "Window_Association_Buzzer",
                                                                controller=self))
        btn_terminer.pack()
        btn_ajouter_equipe = Button(self, text="Effacer une équipe", command=self.erase_team)
        btn_ajouter_equipe.pack()

        btn_ajouter_touche = Button(self, text="Ajouter des touches", command=self.add_key)
        btn_ajouter_touche.pack()


class Window_Association_Buzzer(tk.Frame):
    """
    Classe associée à la fenêtre où l'on associe les équipes à un buzzer
    """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.Obj_Menu_Create_Team = controller
        self.container = controller.container
        tk.Label(self, text="ASSOCIER UNE ÉQUIPE À UN BUZZER").pack()
        tk.Label(self, text="Buzzers:").place(x=70, y=70)
        longueur_y = 115
        self.list_variable_team = {}
        for n in range(0, (len(controller.list_team))):
            nom_buzz = "Buzz0{}".format(str(n))
            tk.Label(self, text=nom_buzz).place(x=45, y=longueur_y)
            variable_team = StringVar(self)
            variable_team.set(controller.list_team[0])  # default value
            self.list_variable_team[n] = variable_team

            drop_down_menu_team = OptionMenu(self, variable_team, *controller.list_team)
            drop_down_menu_team.pack()
            drop_down_menu_team.place(x=100, y=longueur_y)
            longueur_y += 55

        longueur_y += 30

        btn_liste_equipe = Button(self, text="Liste des équipes", command=controller.show_team)
        btn_liste_equipe.place(x=100, y=longueur_y)
        longueur_y += 38
        btn_revenir_menu = Button(self, text="revenir au menu principal",
                                  command=lambda: controller.switch_frame(controller.container, "Menu_Create_Team",
                                                                          controller=self.Obj_Menu_Create_Team))
        btn_revenir_menu.place(x=100, y=longueur_y)
        longueur_y += 38
        btn_jeu = Button(self, text="commencer le jeu",
                         command=lambda: controller.switch_frame(controller.container, "Window_Detect_Winner",
                                                                 controller=self))
        btn_jeu.place(x=100, y=longueur_y)


class Window_Detect_Winner(tk.Frame):
    """
    Classe associée à la fenêtre où l'on attend le buzz d'une équipe
    """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.Obj_Menu_Create_Team = controller.Obj_Menu_Create_Team
        self.Obj_Window_Association_Buzzer = controller
        tk.Label(self, text="EN ATTENTE DU BUZZ.....").pack()
        self.focus_set()
        self.bind("<KeyPress>", self.on_key_press)

    def on_key_press(self, event):
        """
        Fonction qui s'éxécute lorsqu'on appuie sur une touche
        :param event:
        :return:
        """
        for key, value in self.Obj_Menu_Create_Team.dict_key.items():
            if value == event.char:
                self.winner = self.Obj_Window_Association_Buzzer.list_variable_team[key].get()
                self.Obj_Menu_Create_Team.switch_frame(self.Obj_Menu_Create_Team.container, "Window_Show_Winner",
                                                       controller=self)


            else:
                pass


class Window_Show_Winner(tk.Frame):
    """
    Classe associé à la fenêtre qui déclare le premier qui a buzzé
    """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        controller.unbind("<KeyPress>")
        self.Obj_Menu_Create_Team = controller.Obj_Menu_Create_Team
        self.Obj_Window_Association_Buzzer = controller.Obj_Window_Association_Buzzer
        self.Obj_Window_Detect_Winner = controller
        tk.Label(self, text="PREMIER AU BUZZ ").pack()
        tk.Label(self, text=controller.winner).pack()
        btn_continuer = Button(self, text="Continuer", command=lambda: self.Obj_Menu_Create_Team.switch_frame(
            self.Obj_Menu_Create_Team.container, "Window_Detect_Winner",
            controller=self.Obj_Window_Association_Buzzer))
        btn_continuer.pack()
        btn_liste_equipe = Button(self, text="arrêter le jeu et revenir au menu principal",
                                  command=lambda: self.Obj_Menu_Create_Team.switch_frame(self.Obj_Menu_Create_Team
                                                                                         .container, "Menu_Create_Team",
                                                                                         controller=self.Obj_Menu_Create_Team))
        btn_liste_equipe.pack()


if __name__ == "__main__":
    app = Window_General_Function()
    app.mainloop()
