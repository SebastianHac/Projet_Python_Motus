from tkinter import *
import pygame
fenetre = Tk()
fenetre.geometry('1300x900')

#canvas = Canvas(fenetre, width= 1000, height=800, background='ivory')
#canvas.pack(side=TOP, padx=5, pady=5)
lettre1 = "V"
lettre2 = "O"
lettre3 = "I"
lettre4 = "T"
lettre5 = "U"
lettre6 = "R"
lettre7 = "E"
lettre8 = "S"
switch = 0
v_column=0
grille = []
grille_tableau = []
row = 0
tab_histo=[]

mot_var=StringVar()


mot = input("Entrez votre mot : ") # en 8 lettres pour le test
tabmot = list(mot)
print(tabmot) #['v', 'o', 'i', 't', 'u', 'r', 'e', 's']

mot_entry = Entry(fenetre, textvariable= mot_var,font=('calibre',20,'normal')) 
mot_entry.place(x=500,y=700)

def testmot():
    mot_atest=mot_entry.get()
    tab_histo.append(mot_atest)
    print("le mot a tester est : " + mot_atest)
    print(tab_histo)
    mot_var.set('')
    

bouton_envoie=Button(fenetre, text='Tester le mot', command=testmot, height=3, width=30, bg='red')
bouton_envoie.place(x=850,y=690)

myLabel1 = Label(fenetre, width=10,text=lettre1, height=5, bg="red")
myLabel2 = Label(fenetre, width=10,text=lettre2, height=5, bg="white")
myLabel3 = Label(fenetre, width=10,text=lettre3, height=5, bg="white")
myLabel4 = Label(fenetre, width=10,text=lettre4, height=5, bg="white")
myLabel5 = Label(fenetre, width=10,text=lettre5, height=5, bg="white")
myLabel6 = Label(fenetre, width=10,text=lettre6, height=5, bg="white")
myLabel7 = Label(fenetre, width=10,text=lettre7, height=5, bg="white")
myLabel8 = Label(fenetre, width=10,text=lettre8, height=5, bg="white")

"""
myLabel1.grid(row=0, column=0)
myLabel1.place(x=500, y=200)
myLabel2.grid(row=0, column=1)
myLabel2.place(x=575, y=200)
myLabel3.grid(row=0, column=2)
myLabel3.place(x=650, y=200)
myLabel4.grid(row=0, column=3)
myLabel4.place(x=725, y=200)
myLabel5.grid(row=0, column=4)
myLabel5.place(x=800, y=200)
myLabel6.grid(row=0, column=5)
myLabel6.place(x=875, y=200)
myLabel7.grid(row=0, column=6)
myLabel7.place(x=950, y=200)
myLabel8.grid(row=0, column=7)
myLabel8.place(x=1025, y=200)

grille.append(grille_tableau)
print(grille)
"""
x=500
y=200
for i in range(0, 8):
    grille_tableau.append(tabmot[i])
    myLabel=Label(fenetre, width=10, height=5, text=tabmot[i], bg="white")
    myLabel.grid(row=0, column=v_column)
    myLabel.place(x=x,y=y)
    x+=75
    v_column += 1
    switch += 1
print(grille)



'''myLabel1 = Label(fenetre, width=10, height=5, text=lettre1, bg="blue")
myLabel2 = Label(fenetre, width=10, height=5, text=lettre2, bg="red")
myLabel3 = Label(fenetre, width=10, height=5, text=lettre3, bg="blue")
myLabel4 = Label(fenetre, width=10, height=5, text=lettre4, bg="red")
myLabel5 = Label(fenetre, width=10, height=5, text=lettre5, bg="blue")
myLabel6 = Label(fenetre, width=10, height=5, text=lettre6, bg="red")
myLabel7 = Label(fenetre, width=10, height=5, text=lettre7, bg="blue")
myLabel8 = Label(fenetre, width=10, height=5, text=lettre8, bg="red")'''

fenetre.mainloop()