import sys
import pygame
from Grille import Grille


class Case:
    def __init__(self):
        self.value = ''
        self.size_x = 75
        self.size_y = 75
        self.position_x = 0
        self.position_y = 0
        # self.color = '' en hexadécimal


class Partie:  # Classe qui permet de lancer une partie
    """ Classe game """

    def __init__(self):  # fonction principale de la partie
        pygame.display.set_caption("Motus remastered")  # titre
        self.partie_en_cours = True  # True quand en cours, False pour leave
        self.screen = pygame.display.set_mode((1200, 900))  # fenetre + taille
        self.grille = Grille(self.screen)

    def jeu_en_cours(self):
        """ Jeu en cours ou non """
        while self.partie_en_cours:
            for event in pygame.event.get():  # gere les évenements tant que le jeu est en cours
                if event.type == pygame.QUIT:
                    sys.exit()  # quitte le jeu

            self.screen.fill((255, 255, 255))
            self.grille.afficher_grille()
            pygame.display.flip()  # met à jour ecran après event

