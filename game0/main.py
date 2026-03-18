import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800,400)) # Set Display Surface (Screen)
pygame.display.set_caption("OJO's Game") # Game Title
clock = pygame.time.Clock() # Set clock object
test_font = pygame.font.Font('font/Pixeltype.ttf', 50) # Set Font
game_active = True # Set game state

# test_surface = pygame.Surface((100,200))
# test_surface.fill('Red') #Surface color

# Sky/Ground Surfaces
sky_surf = pygame.image.load('graphics/Sky.png').convert()
ground_surf = pygame.image.load('graphics/ground.png').convert()

# Score Surf/Rect
score_surf = test_font.render("OJO's Game", False, (64,64,64))
score_rect = score_surf.get_rect(center = (400,50))

# Snail Surface and Rectangle
snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(bottomright = (600, 300))

# Player Surface and Rectangle
player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 300))

player_gravity = 0

# Event While Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Mouse Collision Test
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos):
        #         print("collision")

        if game_active:
            # Click to PLayer to Jump 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    player_gravity = -20

            # Space to Jump
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20

            if event.type == pygame.KEYUP:
                print('key up')

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800
        
    
    if game_active:
        # blit = Block Image Transfer
        screen.blit(sky_surf,(0,0))
        screen.blit(ground_surf,(0,300))
        pygame.draw.rect(screen, '#c0e8ec', score_rect)
        pygame.draw.rect(screen,'#c0e8ec', score_rect,30)
        screen.blit(score_surf, score_rect)


        # YAY Shapes!
        # pygame.draw.aaline(screen,'Black', (0,0),(800,400), 5)
        # pygame.draw.aaline(screen,'Black', (0,0),pygame.mouse.get_pos(), 5)
        # pygame.draw.ellipse(screen, "Brown", pygame.Rect(50,200,100,100))

        # Snail
        snail_rect.x -= 4
        if snail_rect.right <= 0: snail_rect.left = 800
        screen.blit(snail_surf,(snail_rect))
        

        # JUMP Test
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_SPACE]:
        #     print('jump')

        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surf,player_rect)
        

        # Collision
        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill('Yellow')


    # Collision Test
    # if player_rect.colliderect(snail_rect):
    #     print('collision')

    # Click Test
    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint((mouse_pos)):
    #     print(pygame.mouse.get_pressed())

    pygame.display.update()
    # Set Max Frame rate
    clock.tick(60)