""" doc """

import pygame

 

class Grille: #Classe qui gere la grille
    """ doc"""
    # Define some colors
    
    def __init__(self,screen):
        self.screen=screen
        '''
        self.lignes=[((300,100),(1100,100)),
                       ((300,200),(1100,200)),
                       ((300,300),(1100,300)),
                       ((300,400),(1100,400)),
                       ((300,500),(1100,500)),
                       ((300,600),(1100,600)),
                       ((300,700),(1100,700)),]
        # Liste de lignes pour faire une grille

        self.colonnes=[( (300,100),(300,700) ),
                     ( (400,100),(400,700) ),
                     ( (500,100),(500,700) ),
                     ( (600,100),(600,700) ),
                     ( (700,100),(700,700) ),
                     ( (800,100),(800,700) ),
                     ( (900,100),(900,700) ),
                     ( (1000,100),(1000,700) ), 
                     ( (1100,100),(1100,700) ),]
        '''
       

    def afficher_grille(self):
        """doc"""
        '''
        for ligne in self.lignes:
            pygame.draw.line(self.screen,(0,0,0), ligne[0], ligne[1],1)
        for colonne in self.colonnes:
            pygame.draw.line(self.screen,(0,0,0), colonne[0], colonne[1],1)
        '''

        black = (0, 0, 0)
        white = (255, 255, 255)
        green = (0, 255, 0)
        red = (255, 0, 0)
        beige=(200,173,127)
 
        # This sets the WIDTH and HEIGHT of each grid location
        width = 75
        height = 75
        ecart_x=440
        ecart_y=100
        valeur_x = 0
        valeur_y = 0
 
        # This sets the margin between each cell
        margin = 5
            # --- Create grid of numbers
            # Create an empty list
        grille = []
            # Loop for each ligne
        for ligne in range(8):
            # For each ligne, create a list that will
            # represent an entire ligne
            grille.append([])
            # Loop for each colonne
            for colonne in range(8):
            # Add a the number zero to the current ligne
                grille[ligne].append(0)

        for ligne in range(8):
            for colonne in range(8):
                color = white
                
                pygame.draw.rect(self.screen,
                            color,
                            [ecart_x+(margin + width) * colonne + margin,
                            ecart_y+(margin + height) * ligne + margin,
                            width,
                            height])  

  