from tkinter import *
from tkinter import messagebox
import pygame

fenetre = Tk()
fenetre.geometry('1300x900')
fenetre['background'] = 'cyan'
titre = Text(fenetre)
titre.insert(INSERT, " Bienvenue dans MOTUS ")
lines_info = ['Bienvenue dans le jeu MOTUS !', 'Règles du jeu :','Tout d'+"'"+'abord, votre adversaire entrera un mot à l'  +
 "'" + 'endroit prévu, vous allez devoir deviner ce mot par la suite . Ce mot ne doit pas contenir de chiffre, ou tout autre caractère n'+"'" +'étant pas une lettre' ,
'Une fois ce mot choisi, il vous sera impossible de le changer', 'Pour tester un mot, entrez celui-ci dans l'+"'" + 'espace dédié à coté du boutton, et cliquez sur ce même boutton ' +"'" + 'Tester le mot' +"'",
'Une fois le mot entré, celui-ci s'+"'" +'affichera dans la grille', 'Si la case contenant une lettre devient rouge, c'+"'" +'est que cette lettre est juste et à la bonne place !',
'Si celle-ci devient jaune, cette lettre est bien dans le mot, mais mal placée ! Vous êtes proche du but ! ', 'Si au contraire, cette lettre reste blanche, c'+"'" +
'est que celle-ci n'+"'" +'est pas dans le mot recherché, dommage !','Vous avez 6 essais pour retrouver le mot de votre adversaire, sans quoi la défaite est imminente.','Bon Jeu !' ]
messagebox.showinfo("Règles du jeu", "\n\n".join(lines_info))

# canvas = Canvas(fenetre, width= 1000, height=800, background='ivory')
# canvas.pack(side=TOP, padx=5, pady=5)
solution = ''

grille = []
grille_tableau = []
row = 0
tab_histo = []
tabmot = []
mot_var = StringVar()
mot_solution = StringVar()
ligne = 0
y = 200
nombre_essai = 0
mot_soluce=''

# mot = input("Entrez votre mot : ") # en 8 lettres pour le test
# tabmot = list(mot)
# print(tabmot) #['v', 'o', 'i', 't', 'u', 'r', 'e', 's']


def enregistrer_solution():
    if (input_solution.get()).isalpha() and len(input_solution.get()) == 8:
        global solution
        solution = input_solution.get()
        solution = list(solution)
        mot_solution.set('')
        bouton_solution.destroy()
        input_solution.destroy()
        bouton_envoie.place(x=850, y=740) # affiche le bouton + champ texte pour tester le mot après qu'il ai envoyé la solution
        mot_entry.place(x=500, y=750)

def testmot():
    global mot_soluce
    global nombre_essai
    if nombre_essai < 6:
        x = 500
        global y
        v_column = 0
        global ligne
        switch = 0
        mot_atest = mot_entry.get()
        tab_histo.append(mot_atest)
        tabmot = list(mot_atest)
        #print("le mot a tester est : " + mot_atest)
        print(tabmot)
        print(tab_histo)
        mot_var.set('')
        for i in range(0, len(mot_atest)):
            test_bool = False
            if tabmot[i] == solution[i]:
                myLabel = Label(fenetre, width=10, height=5, text=tabmot[i], bg="red")
                myLabel.grid(row=ligne, column=v_column)
                myLabel.place(x=x, y=y)
                x += 80
                v_column += 1
                switch += 1
                #print('correct')
            else:
                for element in solution:
                    if tabmot[i] == element:
                        test_bool = True
                        break
                if tabmot[i] != solution[i] and test_bool == True:
                    myLabel = Label(fenetre, width=10, height=5, text=tabmot[i], bg="yellow")
                    myLabel.grid(row=ligne, column=v_column)
                    myLabel.place(x=x, y=y)
                    x += 80
                    v_column += 1
                    switch += 1
                    #print('mauvaise place')
                else:
                    myLabel = Label(fenetre, width=10, height=5, text=tabmot[i], bg="white")
                    myLabel.grid(row=ligne, column=v_column)
                    myLabel.place(x=x, y=y)
                    x += 80
                    v_column += 1
                    switch += 1
                    #print('incorrect')



        y += 85
        ligne += 1
        print(ligne)
    nombre_essai += 1

    for i in solution:
        mot_soluce+=i
        
    print(mot_soluce)
    for elem in tab_histo:
        if mot_soluce==elem:
            messagebox.showinfo('Bien joué','Félicitation, vous avez trouvé le mot !')
            fenetre.quit()
        mot_soluce=''
    
    if nombre_essai==6:
        messagebox.showinfo('Dommage','Nombre maximum d'+"'"+'essais atteind, vous avez perdu')
        fenetre.quit()



# Bouton + champ texte pour écrire le mot à tester

bouton_envoie = Button(fenetre, text='Tester le mot', command=testmot, height=3, width=30, bg='red')

mot_entry = Entry(fenetre, textvariable=mot_var, font=('calibre', 20, 'normal'))


# Bouton + champ texte pour écrire le mot à deviner

bouton_solution = Button(fenetre, text='Confirmez le mot à deviner', command=enregistrer_solution, height=3, width=30, bg='red')
bouton_solution.place(x=542, y=500)
input_solution = Entry(fenetre, textvariable=mot_solution, font=('calibre', 20, 'normal'))
input_solution.place(x=500, y=450)


fenetre.mainloop()