
import pygame
import sys
from Grille import *

class Partie : # Classe qui permet de lancer une partieclass Partie : # Classe qui permet de lancer une partie
    """ Classe game """
    def __init__(self):  #fonction principale de la partie
        
        pygame.display.set_caption("Motus remastered") #titre
        self.partie_en_cours= True # True quand en cours, False pour leave
        self.screen= pygame.display.set_mode((1500,1000)) # fenetre + taille
        self.grille = Grille(self.screen)
        
    def jeu_en_cours(self): 
        """ Jeu en cours ou non """
        
        white = (255, 255, 255)
        black = (  0,   0,   0)
        green = (0, 255, 0)
        blue = (0, 0, 180)
        red   = (255,   0,   0)

       

        tabmot=[]
        couleurentree=pygame.Color('dodgerblue2')
        
        active = False
        motentre = ''
        font = pygame.font.Font(None, 32)
        input_box = pygame.Rect(570, 800, 400, 50)
        couleurchamp=(0,0,0)
        position_x=475
        position_y=135
        valeur_x = 75
        valeur_y = 75
        mot_cop=''
        while self.partie_en_cours:
            text = font.render(mot_cop, True, black)
            recText=text.get_rect()
            for event in pygame.event.get(): #gere les évenements tant que le jeu est en cours
                if event.type== pygame.QUIT: 
                    sys.exit()  #quitte le jeu
                if event.type == pygame.MOUSEBUTTONDOWN:
                # Si l'utilisateur clique sur l'input
                    if input_box.collidepoint(event.pos):
                    # Donne la possibilité d'écrire dans le champ texte.
                        active = not active
                    else:
                        active = False
                        
                        
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            
                            print(motentre)
                            tabmot+=motentre
                            print(tabmot)
                            
                            pygame.display.flip()
                        elif event.key == pygame.K_BACKSPACE:
                            motentre = motentre[:-1]
                        else:
                            motentre += event.unicode
            for i in tabmot:
                mot_cop+=i
            
            self.screen.blit(text, (position_x,position_y))
            pygame.display.flip()
            tabmot=[]
            self.screen.fill((200,173,127))
            #remplir champ texte
            txt_surface = font.render(motentre, True, couleurchamp)
            self.screen.blit(txt_surface, (input_box.x+20, input_box.y+15))
            self.grille.afficher_grille()
            pygame.draw.rect(self.screen, couleurentree, input_box, 2)

        #self.screen.blit(text_surface_obj, text_rect_obj)
        