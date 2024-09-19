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
font = pygame.font.Font(join("Assets", "Franxurter.ttf"), 32)

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

game_over_text = font.render("GAMEOVER", True, BLUE, YELLOW)
game_over_text_rect = game_over_text.get_rect()
game_over_text_rect.center = (WIDTH / 2, HEIGHT / 2)

continue_text = font.render("Click anywhere to play again", True, YELLOW, BLUE)
continue_text_rect = continue_text.get_rect()
continue_text_rect.center = (WIDTH / 2, HEIGHT / 2 + 64)

#Load Sound and Music
clicker_sound = pygame.mixer.Sound(join("Assets", "click_sound.wav"))
clicker_sound.set_volume(.25)
miss_sound = pygame.mixer.Sound(join("Assets", "miss_sound.wav"))
miss_sound.set_volume(.25)
background_music = join("Assets", "ctc_background_music.wav")
pygame.mixer.music.load(background_music)
pygame.mixer.music.set_volume(.5)

#Load Images
background_image = pygame.image.load(join("Assets", "background.png")).convert_alpha()
background_image_rect = background_image.get_rect()
background_image_rect.topleft = (0, 0)

clown_image = pygame.image.load(join("Assets", "clown.png")).convert_alpha()
clown_image_rect = clown_image.get_rect()
clown_image_rect.center = (WIDTH / 2, HEIGHT / 2)

#Main game loop
pygame.mixer.music.play(-1, 0.0)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #A click is made
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]

            # The clown was clicked
            if clown_image_rect.collidepoint(mouse_x, mouse_y):
                clicker_sound.play()
                score += 1
                clown_velocity += CLOWN_ACCERLATION

                #move the clown in a new direction
                previous_dx = clown_dx
                previous_dy = clown_dy
                while previous_dx == clown_dx and previous_dy == clown_dy:
                    clown_dx = random.choice([-1, 1])
                    clown_dy = random.choice([-1, 1])
            #Missed the clown
            else:
                miss_sound.play()
                player_lives -= 1

    #Move the Clown
    clown_image_rect.x += clown_dx * clown_velocity
    clown_image_rect.y += clown_dy * clown_velocity

    #Bounce off the edges of display
    if clown_image_rect.left <= 0 or clown_image_rect.right >= WIDTH:
        clown_dx = -1 * clown_dx
    if clown_image_rect.top <= 0 or clown_image_rect.bottom >= HEIGHT:
        clown_dy = -1 * clown_dy

    #Blit Background
    display_surface.blit(background_image, background_image_rect)

    #Blit Hud
    display_surface.blit(title_text, title_text_rect)
    display_surface.blit(score_text, score_text_rect)
    display_surface.blit(lives_text, lives_text_rect)

    #Blit Assets
    display_surface.blit(clown_image, clown_image_rect)

    #Update Display
    pygame.display.update()
    clock.tick(FPS)



#End the game
pygame.quit()