import pygame, sys, random
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
PLAYER_STARTING_LIVES = 5
CLOWN_STARTING_VELOCITY = 3 
CLOWN_ACCERLATION = .5

score = 0 
player_lives = PLAYER_STARTING_LIVES

clown_velocity = CLOWN_STARTING_VELOCITY
clown_dx = random.choice([-1, 1])
clown_dy = random.choice([-1, 1])

#Set Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (1, 175, 209)
YELLOW = (248, 231, 28)

#Set Fonts
font = pygame.font.Font(join("Assets", "Franxurter.ttf"))

#Set text
TITLE_TEXT = "Catch The Clown"
title_text = font.render(TITLE_TEXT, True, BLUE)
title_text_rect = title_text.get_rect()
title_text_rect.topleft = (50, 10)

score_text = font.render(f"Score: {score}", True, YELLOW)
score_text_rect = score_text.get_rect()
score_text_rect.topright = (WIDTH - 50, 10)

lives_text = font.render(f"Lives: {player_lives}", True, YELLOW)
lives_text_rect = lives_text.get_rect()
lives_text_rect.topright = (WIDTH - 50, 50)

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