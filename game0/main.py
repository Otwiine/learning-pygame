import pygame
from sys import exit
from random import randint

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time 
    score_surf = test_font.render(f'Score: {current_time}',False,(64,64,64))
    score_rect = score_surf.get_rect(center = (400,60))
    screen.blit(score_surf, score_rect)
    return current_time
    # print(current_time)

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            screen.blit(snail_surf, obstacle_rect)
        return obstacle_list
    else: return []

pygame.init()

screen = pygame.display.set_mode((800,400)) # Set Display Surface (Screen)
pygame.display.set_caption("OJO's Runner") # Game Title
clock = pygame.time.Clock() # Set clock object
test_font = pygame.font.Font('font/Pixeltype.ttf', 50) # Set Font
game_active = False # Set game state
start_time = 0
score = 0

# test_surface = pygame.Surface((100,200))
# test_surface.fill('Red') #Surface color

# Sky/Ground Surfaces
sky_surf = pygame.image.load('graphics/Sky.png').convert()
ground_surf = pygame.image.load('graphics/ground.png').convert()

# Score Surf/Rect
# score_surf = test_font.render("OJO's Game", False, (64,64,64))
# score_rect = score_surf.get_rect(center = (400,50))

# Snail Surface and Rectangle (Obstacles)
snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(bottomright = (600, 300))

obstacle_rect_list = []

# Player Surface and Rectangle
player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 300))
player_gravity = 0

# Intro Screen
player_stand = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
# player_stand = pygame.transform.scale2x(player_stand)
player_stand = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand.get_rect(center = (400,200))

name_surf = test_font.render("OJO's Runner",False,(111,196,169))
name_rect = name_surf.get_rect(center = (400,50))


instruction_surf = test_font.render("Press SPACE to run",False,(111,196,169))
instruction_rect = instruction_surf.get_rect(center = (400,350))

# Timer 
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)



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

            # if event.type == pygame.KEYUP:
            #     print('key up')

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800
                start_time = int(pygame.time.get_ticks() / 1000)

        if event.type == obstacle_timer and game_active:
            obstacle_rect_list.append(snail_surf.get_rect(bottomright = (randint(900,1100), 300)))
        
    
    if game_active:
        # blit = Block Image Transfer
        screen.blit(sky_surf,(0,0))
        screen.blit(ground_surf,(0,300))
        # pygame.draw.rect(screen, '#c0e8ec', score_rect)
        # pygame.draw.rect(screen,'#c0e8ec', score_rect,30)
        # screen.blit(score_surf, score_rect)
        score = display_score()


        # YAY Shapes!
        # pygame.draw.aaline(screen,'Black', (0,0),(800,400), 5)
        # pygame.draw.aaline(screen,'Black', (0,0),pygame.mouse.get_pos(), 5)
        # pygame.draw.ellipse(screen, "Brown", pygame.Rect(50,200,100,100))

        # Basic Snail
        # snail_rect.x -= 8
        # if snail_rect.right <= 0: snail_rect.left = 800
        # screen.blit(snail_surf,(snail_rect))
        

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

        # Obstacle Movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        
        

        # Collision
        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill((94,129,162))
        screen.blit(player_stand,player_stand_rect)

        score_message = test_font.render(f"Your Score: {score}",False,(111,196,169))
        score_message_rect = score_message.get_rect(center = (400,350))
        screen.blit(name_surf, name_rect)

        if score == 0:
            screen.blit(instruction_surf,instruction_rect)

        else:
            screen.blit(score_message,score_message_rect)

        


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