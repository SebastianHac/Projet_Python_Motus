#REGLES : vu que pas d'affichage graphique : mot testé : si place ok : ecrit en MAJ
# si lettre dedans mais pas bien placée : low
# si pas dedans : point

mot_adeviner=""
while len(mot_adeviner) != 8:
    mot_adeviner = input("entrez un mot de 8 lettres : ").lower();
mot_atest = ""
nombre_essai=0
while nombre_essai<7: #marche pas
    while mot_atest != mot_adeviner:
        #Manque boucle pour tester que mot_atest fait 8 lettres mais fait planter
        mot_atest= input("Entrez un mot à tester de 8 lettres : ").lower(); #mot a tester
        copie_adeviner=mot_adeviner #copie pour modif au fur et à mesure pour trouver le mot
        affichage="--------" #affichage du mot final
        copie_atest = mot_atest  #copie du mot entré, pour pouvoir modifier affichage

        for i in range(8):    #boucle test si bonne lettre et si bonne place, remplace par la lettre en maj si ok
            if copie_adeviner[i] ==  copie_atest[i]:
                affichage = affichage[:i]+copie_atest[i].upper() + affichage[i+1:] #remplace le - par la lettre en maj 
                copie_adeviner = copie_adeviner[:i] + "^" + copie_adeviner[i+1:] # Pour que si le carac se trouve deux fois dedans, le prochain test prenne pas compte d'elle 
                copie_atest = copie_atest[:i] + "#" + copie_atest[i+1:]

            # print(copie_adeviner)
            # print(copie_atest)

        for i in range(8):  # boucle qui test si la lettre est dans le mot, sachant que si elle est à la bonne place elle sera déjà en maj avec boucle du haut
            if copie_atest[i] in copie_adeviner:
                affichage =  affichage[:i]+copie_atest[i]+affichage[i+1:]
                indice = copie_adeviner.find(copie_atest[i]) #trouve indice de la lettre male placée 
            #print(indice)
                copie_adeviner=copie_adeviner[:indice] + "^" + copie_adeviner[indice+1:] #même principe qu'au dessus

            elif affichage[i] =='-': #remplace les derniers carac restants, donc logiquement ceux qui ne sont pas dans le mot par un point
                affichage=affichage[:i]+'-'+affichage[i+1:]
        nombre_essai+=1
        print(nombre_essai)
   

        print("voici le mot : " + mot_adeviner)
        print("voici le mot corrigé : " +affichage )
print("bien joué vous avez trouvé le mot : " + mot_adeviner)