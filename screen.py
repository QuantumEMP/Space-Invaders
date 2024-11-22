import pygame
import os

pygame.init()
screen = pygame.display.set_mode((800,800))
bg = pygame.image.load(os.path.join('assests','bg.jpg')).convert()
icon = pygame.image.load(os.path.join('assests','bg.jpg'))
pygame.display.set_caption('Space Invaders: Last Man Standing')
pygame.display.set_icon(icon)
screen.blit(bg,(0,0))
pygame.display.flip()
status = True
while (status):
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            status = False

pygame.quit()