import pygame
import pygame.locals

class Enemy:
    def __init__(self,type,image) -> None:
        self.image = pygame.image.load(image).convert()
        self.type = type
    
    def behavior(self):
        pass
        #if self.type == whatever type
            #run func
        #elif...

    #def whatevertype(self):
        #set behavior

class Player:
    def __init__(self) -> None:
        #self.image = pygame.image.load('''image''').convert()
        pass

    def movement(self):
        pass

    def collision(self):
        pass

    def death(self):
        pass

    #def powerup1(self):
        #set behavior
    
    #def powerup2(self):
        #set behavior
    
    #def ...
