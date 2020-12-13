import pygame
import sys
from Grille import *

class Partie : # Classe qui permet de lancer une partieclass Partie : # Classe qui permet de lancer une partie
    """ Classe game """
    def __init__(self):  #fonction principale de la partie
        
        pygame.display.set_caption("Motus remastered") #titre
        self.partie_en_cours= True # True quand en cours, False pour leave
        self.screen= pygame.display.set_mode((1200,900)) # fenetre + taille
        self.grille = Grille(self.screen)

    def jeu_en_cours(self): 
        """ Jeu en cours ou non """
        
        couleurentree=pygame.Color('dodgerblue2')
        
        active = False
        motentre = ''
        font = pygame.font.Font(None, 32)
        
        input_box = pygame.Rect(525, 700, 250, 50)
        couleurchamp=(255,0,0)
        while self.partie_en_cours:
           
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
                        # Change the current color of the input box.
                        
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            print(motentre)
                            motentre = ''
                        elif event.key == pygame.K_BACKSPACE:
                            motentre = motentre[:-1]
                        else:
                            motentre += event.unicode
            self.screen.fill((255,255,255))
            txt_surface = font.render(motentre, True, couleurchamp)
            self.screen.blit(txt_surface, (input_box.x+20, input_box.y+15))
            self.grille.afficher_grille()
            pygame.draw.rect(self.screen, couleurentree, input_box, 2)
            pygame.display.flip() #met à jour ecran après event 

if __name__=='__main__':
    pygame.init()
    Partie().jeu_en_cours()
    pygame.quit()