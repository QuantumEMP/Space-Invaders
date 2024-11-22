import pygame
from screen import display_screen

pygame.init()
display_screen()
status = True
while (status):
    
    for i in pygame.event.get():
        
        if i.type == pygame.QUIT:
            status = False

pygame.quit()