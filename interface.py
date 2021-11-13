# -*- coding: utf-8 -*-
'''
Projet Python S1-L1 2021
Collaboration : Lucas Escoubes / Nathan Danis

Création du fichier : 09/11/2021 11:40

Le fichier générant l'interface Tkinter du programme, est obligé d'être dans un fichier a part (mélangeant
function, variables et programme principal) car sinon le programme ne peut pas fonctionner à cause d'un problème
de boucle et d'appel non respecté.

'''
################################################################################################################
################################################## INTERFACE ###################################################
################################################################################################################
from tkinter import *
from variable import *

# ------ WINDOW SETTINGS ------ #
fenetre = Tk()                                  # définission de la fenetre
fenetre.title("Library")                        # titre de la fenetre
fenetre.geometry("800x600")                     # taille de la fenetre
fenetre.minsize(width="800", height="600")      # taille minimum de la fenetre

#création d'un menu
def MenuBar():
    # ------ Menu déroulant ------ #
    label = Label(fenetre, text="Welcome to your bookstore \n Find your happiness with our recommendation")
    label.place(relx=0.5, y= 20,anchor=CENTER)

    butonExit=Button(fenetre, text="🏠 Home", command=WelcomePage)
    butonExit.place(x = 0, y = 0)

def WelcomePage():
    for c in fenetre.winfo_children():
        c.destroy()

    # ------ CONTENT WINDOW ------ #
    MenuBar()

    butonPageProfil=Button(fenetre, text="👤 Profil user", command=ProfilPage)
    butonPageProfil.place(relx=0.25, y = 100, anchor=CENTER)

    butonVisitBookDepository=Button(fenetre, text="📚 Book Depository", command=DepositoryPage)
    butonVisitBookDepository.place(relx=0.5, y = 100, anchor=CENTER)

    butonRecommandation=Button(fenetre, text="📈 Recommandation", command=RecommandationPage)
    butonRecommandation.place(relx=0.75, y = 100, anchor=CENTER) 
    
def ProfilPage():
    for c in fenetre.winfo_children():
        c.destroy()

    MenuBar()

    butonAddUser=Button(fenetre, text="➕ Add a user", command=AddUser)
    butonAddUser.place(relx=0.20, y = 100, anchor=CENTER) 

    butonShowUser=Button(fenetre, text="📖 Show a user", command=fenetre.quit)
    butonShowUser.place(relx=0.40, y = 100, anchor=CENTER) 

    butonModifyUser=Button(fenetre, text="📝 Modify a user", command=fenetre.quit)
    butonModifyUser.place(relx=0.6, y = 100, anchor=CENTER) 

    butonDeleteUser=Button(fenetre, text="🚮 Delete a user", command=fenetre.quit)
    butonDeleteUser.place(relx=0.8, y = 100, anchor=CENTER) 

def DepositoryPage():
    for c in fenetre.winfo_children():
        c.destroy()

    MenuBar()

def RecommandationPage():
    for c in fenetre.winfo_children():
        c.destroy()

    MenuBar()

def AddUser():
    for c in fenetre.winfo_children():
        c.destroy()

    MenuBar()

    # -- Pseudo -- #
    labelPseudo = Label(fenetre, text="Pseudo* :")
    labelPseudo.place(x = 30, y = 90)

    varPseudo=StringVar(None)
    textPseudo=Entry(fenetre,textvariable=varPseudo,width=15)
    textPseudo.place(x = 100, y = 90)


    # -- Gender -- #
    labelGender = Label(fenetre, text="Gender* :")
    labelGender.place(x = 30, y = 130)

    userGender = StringVar()
    userGender.set(user_gender[0])
    optionGender = OptionMenu(fenetre, userGender, *user_gender)
    optionGender.place(x = 100, y = 130)


    # -- Age -- #
    labelAge = Label(fenetre, text="Age* :")
    labelAge.place(x = 270, y = 90)

    userAge = StringVar()
    userAge.set(user_age[0])
    optionAge = OptionMenu(fenetre, userAge, *user_age)
    optionAge.place(x = 340, y = 90)


    # -- Book Style -- #
    labelStyle = Label(fenetre, text="Lecture's style* :")
    labelStyle.place(x = 270, y = 130)

    bookStyle = StringVar()
    bookStyle.set(book_style[0])
    optionGender = OptionMenu(fenetre, bookStyle, *book_style)
    optionGender.place(x = 400, y = 130)

    butonSave=Button(fenetre, text="✅ Save", command=None)
    butonSave.place(relx=0.75, y = 400, anchor=CENTER)



# ------ WINDOW PROJECTION ------ #
WelcomePage()
fenetre.mainloop()