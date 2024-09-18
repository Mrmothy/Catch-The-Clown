import pygame, sys
from os.path import join

#Initialize Pygame
pygame.init()

#Initialize Game Window
WIDTH, HEIGHT = 945, 600
display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch The Clown")


#Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            





#End the game
pygame.quit()