from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk 
import pygame

fenetre = Tk()
fenetre.geometry('1300x900')
fenetre['background'] = 'cyan'
titre = Text(fenetre)
titre.insert(INSERT, " Bienvenue dans MOTUS ")


# canvas = Canvas(fenetre, width= 1000, height=800, background='ivory')
# canvas.pack(side=TOP, padx=5, pady=5)
tab_test_str = ''
tab_test = ['_','_','_','_','_','_','_','_']
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


def enregistrer_solution(): #fonction qui enrégistre le mot que l'adversaire devra trouver
    if (input_solution.get()).isalpha() and len(input_solution.get()) == 8:#test longueur et mot sans chiffre / carac spéciaux
        global text_infos
        global solution
        solution = input_solution.get().lower()#conversion en min au cas où le joueur entre des maj
        solution = list(solution)
        mot_solution.set('')
        bouton_solution.destroy() #retire le bouton après la validation
        input_solution.destroy() #retire l'input après validation
        bouton_envoie.place(x=850, y=740) # affiche le bouton + champ texte pour tester le mot après qu'il ai envoyé la solution
        mot_entry.place(x=500, y=750)
        text_infos.destroy() #retire règles après validation
def testmot():
    global mot_soluce
    global nombre_essai
    if nombre_essai < 6: #condition de victoire basé sur le nombre d'essai
        x = 500
        global y
        v_column = 0
        global ligne 
        mot_atest = mot_entry.get().lower() #conversion en min au cas où le joueur entre des maj
        tab_histo.append(mot_atest)
        tabmot = list(mot_atest)
        #print("le mot a tester est : " + mot_atest)
        #print(tabmot)
        #print(tab_histo)
        mot_var.set('')
        for i in range(0, len(mot_atest)): #bouicle qui va parcourir le mot
            test_bool = False 
            if tabmot[i] == solution[i]: #vérification bonne lettre et bon place
                myLabel = Label(fenetre, width=10, height=5, text=tabmot[i], bg="red") #case de la grille en rouge 
                myLabel.grid(row=ligne, column=v_column) #choix de la case d'affichage
                myLabel.place(x=x, y=y)
                x += 80
                v_column += 1
                
                tab_test[i]=tabmot[i] #pour récup les lettres correctes du mot à deviner et l'afficher au fur et à mesure
                #print('correct')

            else: #test si lettre est dans le mot, mais pas au bon endroit
                for element in solution:
                    if tabmot[i] == element:
                        test_bool = True #si lettre correspond à une lettre mais pas au bon endroit, il stop de chercher sinon écriture de la lettre x8
                        break

                if test_bool == True: #si lettre dedans mais pas bonne place
                    myLabel = Label(fenetre, width=10, height=5, text=tabmot[i], bg="yellow") #case de la grille en blanc
                    myLabel.grid(row=ligne, column=v_column)
                    myLabel.place(x=x, y=y)
                    x += 80
                    v_column += 1
                    
                    #print('mauvaise place')
                else:
                    myLabel = Label(fenetre, width=10, height=5, text=tabmot[i], bg="white") #reste en blanc si lettre pas dans le mot
                    myLabel.grid(row=ligne, column=v_column)
                    myLabel.place(x=x, y=y)
                    x += 80
                    v_column += 1
                    
                    #print('incorrect')
        #boucle pour tester le mot pour l'afficher
        y += 85 #changement colonne
        ligne += 1#ligne 
        #print(ligne)
    
    

        for element in tab_test: # pour noter au fur et à mesure le mot au dessus de la grille
            global tab_test_str
            tab_test_str += element + ' '
        #print(tab_test_str)
        

        #affichage mot
    
        zone_mot= zone_nombre_essai= Canvas(fenetre, bg='cyan', height=50, width=250) #creation du canvas
        zone_mot.create_text(130,26,text=tab_test_str, fill="red",font=('arial',20)) #texte qu'il contient
        zone_mot.place(x=732,y=73) #placement canvas

        #incrémente le nombre d'essais
        nombre_essai += 1
        
        tab_test_str=""#remise à 0 pour pas concatener 

    for i in solution:
        mot_soluce+=i

    #print(mot_soluce)

    #alerte si victoire ou défaite
    for elem in tab_histo:
        if mot_soluce==elem:
            messagebox.showinfo('Bien joué','Félicitation, vous avez trouvé le mot après ' + str(nombre_essai) +' essais !')
            fenetre.quit()
    mot_soluce=''
    
    if nombre_essai==6:
        messagebox.showinfo('Dommage','Nombre maximum d'+"'"+'essais atteind, vous avez perdu.')
        fenetre.quit()

    

    #affichage nombre d'essai

    zone_nombre_essai= Canvas(fenetre, bg='yellow', height=50, width=150) #creation du canvas
    zone_nombre_essai.create_text(75,26,text=("Essai numéro : "+ str(nombre_essai)), fill="red") #texte qu'il contient
    zone_nombre_essai.place(x=1100,y=740) #placement canvas
    

#affichage des règles au début du jeu
text_infos=Label(fenetre, height=30, anchor='se', justify=LEFT, bg='cyan',text=" \n Bienvenue dans le jeu MOTUS ! \n\n Règles du jeu : \n\n\n Tout d'abord votre adversaire entre un mot dans le formulaire juste en bas. Vous allez ensuite devoir deviner ce mot. \n\n Ce mot ne doit contenir ni chiffres ni caractères spéciaux. \n\n Une fois le mot choisit, il vous sera impossible de le changer. \n\n\n Pour tester un mot , entrez celui-ci dans l'espace dédié à côté du bouton. \n\n Une fois le mot entré, celui-ci s'affichera dans la grille : \n\n - si la case contenant la lettre devient rouge, c'est que cette lettre est correcte et à la bonne place. \n\n - si la case contenant la lettre devient jaune, c'est que la lettre est bien dans le mot mais à la mauvaise place ! Vous êtes proche du but !                  \n\n - si au contraire la case reste blanche, c'est que celle-ci n'est pas dans le mot recherché, dommage ! \n\n Vous avez 6 essais pour retrouver le mot de votre adversaire , sans quoi la défaite est imminente ! \n\n\n Bon jeu ! ")
text_infos.pack(side=TOP, fill=X)


#affichage image 
image=Image.open('image2.jpg')
photo=ImageTk.PhotoImage(image)
zone= Label(image=photo)
zone.image=PhotoImage
zone.place(x=0,y=-1)

# créatin bouton + champ texte pour écrire le mot à tester
bouton_envoie = Button(fenetre, text='Tester le mot', command=testmot, height=3, width=30, bg='red')

mot_entry = Entry(fenetre, textvariable=mot_var, font=('arial', 20, 'normal'))


#création + affichage bouton et champ texte pour écrire le mot à deviner

bouton_solution = Button(fenetre, text='Confirmez le mot à deviner', command=enregistrer_solution, height=3, width=30, bg='red')
bouton_solution.place(x=767, y=590)
input_solution = Entry(fenetre, textvariable=mot_solution, font=('arial', 20, 'normal'))
input_solution.place(x=725, y=530)


fenetre.mainloop()