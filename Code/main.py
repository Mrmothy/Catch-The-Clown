import pygame, sys
from os.path import join

#Initialize Pygame
pygame.init()

#Initialize Game Window
WIDTH, HEIGHT = 945, 600
display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch The Clown")

#Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

#Set Game Values

#Set Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Set Fonts
font = pygame.font.Font(join("Assets", "Franxurter.ttf"))

#Set text

#Load Sound and Music
clicker_sound = pygame.mixer.Sound(join("Assets", "click_sound.wav"))
miss_sound = pygame.mixer.Sound(join("Assets", "miss_sound.wav"))
background_music = pygame.mixer.music.load(join("Assets", "ctc_background_music.wav"))

#Load Images
background_image = pygame.image.load(join("Assets", "background.png")).convert_alpha()
background_image_rect = background_image.get_rect()
background_image_rect.center = (WIDTH, HEIGHT)

clown_image = pygame.image.load(join("Assets", "clown.png")).convert_alpha()
clown_image_rect = clown_image.get_rect()
clown_image_rect.center = (0,0)

#Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            





#End the game
pygame.quit()