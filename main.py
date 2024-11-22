import pygame
import assests

def display_screen():
    screen = pygame.display.set_mode((800,500))
    background = pygame.image.load('bg.jpg')

pygame.init()
display_screen()