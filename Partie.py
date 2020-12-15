import pygame
import sys
from Grille import *

tab = []

class Partie(Grille):  # Classe qui permet de lancer une partieclass Partie : # Classe qui permet de lancer une partie
    """ Classe game """

    def __init__(self):  # fonction principale de la partie

        pygame.display.set_caption("Motus remastered")  # titre
        self.partie_en_cours = True  # True quand en cours, False pour leave
        self.screen = pygame.display.set_mode((1500, 1000))  # fenetre + taille
        self.grille = Grille(self.screen)
        self.surface_grille = pygame.Surface([645, 645])


    def jeu_en_cours(self):
        """ Jeu en cours ou non """

        white = (255, 255, 255)
        black = (0, 0, 0)
        green = (0, 255, 0)
        blue = (0, 0, 180)
        red = (255, 0, 0)

        tabmot = []
        couleurentree = pygame.Color('dodgerblue2')

        active = False
        motentre = ''
        font = pygame.font.Font(None, 32)
        input_box = pygame.Rect(570, 800, 400, 50)
        couleurchamp = (0, 0, 0)
        position_x = 475
        position_y = 135
        valeur_x = 75
        valeur_y = 75
        mot_cop = ''
        txt_surface = font.render(motentre, True, couleurchamp)


        while self.partie_en_cours:
            text = font.render(mot_cop, True, black)
            recText = text.get_rect()
            for event in pygame.event.get():  # gere les évenements tant que le jeu est en cours
                if event.type == pygame.QUIT:
                    sys.exit()  # quitte le jeu
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
                            tabmot = list(motentre)
                            for i in range(0, 8):
                                arial_font = pygame.font.SysFont("arial", 20)
                                # surface_case = pygame.Surface([75,75])
                                # surface_case.fill((255,0,0))
                                # self.screen.blit(surface_case, [position_x,position_y])
                                surface_ecriture = arial_font.render(tabmot[i].upper(), True, blue)
                                tab.append(surface_ecriture)
                            '''for i in range (0,8):
                                arial_font = pygame.font.SysFont("arial", 20)
                                #surface_case = pygame.Surface([75,75])
                                #surface_case.fill((255,0,0))
                                #self.screen.blit(surface_case, [position_x,position_y])
                                surface_ecriture = arial_font.render(tabmot[i].upper(), True, blue)
                                #print(surface_ecriture)
                                pygame.display.update(self.screen.blit(surface_ecriture, [position_x,position_y]))
                                position_x += 80
                                print(surface_ecriture)
                                pygame.time.wait(500)

                                self.surface_grille.blit(text, (position_x, position_y))
                                self.surface_grille.blit(surface_case, (0, 100))

                                position_x += 75
                                print(position_x)'''
                            print('here')
                        elif event.key == pygame.K_BACKSPACE:
                            motentre = motentre[:-1]
                        else:
                            motentre += event.unicode

            if tabmot != []:
                for i in range (0,8):
                    arial_font = pygame.font.SysFont("arial", 20)
                    # surface_case = pygame.Surface([75,75])
                    # surface_case.fill((255,0,0))
                    # self.screen.blit(surface_case, [position_x,position_y])
                    surface_ecriture = arial_font.render(tabmot[i].upper(), True, blue)
                    tab.append(surface_ecriture)
                    # print(surface_ecriture)
                    pygame.display.update(self.screen.blit(surface_ecriture, [position_x, position_y]))
                    position_x += 80
                    print(surface_ecriture)
                    pygame.time.wait(500)
                print(tab)
                position_x = 475
                #position_y += 80
                '''pygame.display.update(self.screen.blit(tab[0], [position_x, position_y]))
                pygame.display.update(self.screen.blit(tab[1], [position_x + 80, position_y]))
                pygame.display.update(self.screen.blit(tab[2], [position_x + 160, position_y]))
                pygame.display.update(self.screen.blit(tab[3], [position_x + 240, position_y]))
                pygame.display.update(self.screen.blit(tab[4], [position_x + 320, position_y]))
                pygame.display.update(self.screen.blit(tab[5], [position_x + 400, position_y]))
                pygame.display.update(self.screen.blit(tab[6], [position_x + 480, position_y]))
                pygame.display.update(self.screen.blit(tab[7], [position_x + 560, position_y]))'''



            for i in tab:
                position_y = 135
                pygame.display.update(self.screen.blit(i, [position_x, position_y]))
                position_x += 80
            position_x = 475



            pygame.display.flip()
            self.screen.fill((200, 173, 127))
            # remplir champ texte
            txt_surface = font.render(motentre, True, couleurchamp)
            self.screen.blit(txt_surface, (input_box.x + 20, input_box.y + 15))
            self.grille.afficher_grille()
            pygame.draw.rect(self.screen, couleurentree, input_box, 2)

        #self.screen.blit(text_surface_obj, text_rect_obj)surface_obj, text_rect_obj)