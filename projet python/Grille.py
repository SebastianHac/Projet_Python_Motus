""" doc """

import pygame

 

class Grille: #Classe qui gere la grille
    """ doc"""
    def __init__(self,screen):
        self.screen=screen
        self.lignes=[((300,130),(900,130)),
                       ((300,205),(900,205)),
                       ((300,280),(900,280)),
                       ((300,355),(900,355)),
                       ((300,430),(900,430)),
                       ((300,505),(900,505)),
                       ((300,580),(900,580)),]
        # Liste de lignes pour faire une grille

        self.colonnes=[( (300,130),(300,580) ),
                     ( (375,130),(375,580) ),
                     ( (450,130),(450,580) ),
                     ( (525,130),(525,580) ),
                     ( (600,130),(600,580) ),
                     ( (675,130),(675,580) ),
                     ( (750,130),(750,580) ),
                     ( (825,130),(825,580) ), 
                     ( (900,130),(900,580) ),]

    def afficher_grille(self):
        """doc"""
        
        for ligne in self.lignes:
            pygame.draw.line(self.screen,(0,0,0), ligne[0], ligne[1],1)
        for colonne in self.colonnes:
            pygame.draw.line(self.screen,(0,0,0), colonne[0], colonne[1],1)

      