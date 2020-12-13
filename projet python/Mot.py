import pygame

class Mot: #Classe qui gere les mots

        def __init__(self):
           pass

        def recup_mot(self):
            couleurentree=pygame.Color('dodgerblue2')
            active = False
            motentre = ''
            font = pygame.font.Font(None, 32)
        
            input_box = pygame.Rect(450, 700, 300, 50)
            couleurchamp=(255,0,0)