import pygame
from sys import exit
from random import randint

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = test_font.render(f'Score: {current_time}', False, (64,64,64))
    score_rect = score_surface.get_rect(center = (400,50))
    screen.blit(score_surface, score_rect)
    return current_time
    
def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            screen.blit(snail_surface,obstacle_rect)
        
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    
    else:
        return [] 
    
pygame.init() #initializing pygame
screen = pygame.display.set_mode((800, 400)) #args (width, height)
pygame.display.set_caption('My first game')
clock = pygame.time.Clock() #creates a clock object
test_font = pygame.font.Font('static/font/Pixeltype.ttf', 50) #args (font type, font size)
game_active = True
start_time = 0
score = 0

sky_surface = pygame.image.load('static/images/Sky.png').convert() #.convert=it converts to a type of image pygame can work with more easily and makes the game run faster
ground_surface = pygame.image.load('static/images/ground.png').convert()

# score_surface = test_font.render("My Game", False, (64,64,64)) #args (text, Anti-Aliasing, color) AA = smooth edges
# score_rect = score_surface.get_rect(center = (400, 50)) #400 is half of width of screen so it's in the middle and 50 is what we used screen.blit(score_surface, (300,50)) down bellow before

# Obstacles
snail_surface = pygame.image.load('static/images/snail1.png').convert_alpha() #removing alpha values 
snail_rect = snail_surface.get_rect(bottomright = (600,300))

obstacle_rect_list = []

player_surf = pygame.image.load('static/images/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300)) #(topleft=(x,y))
                                                         #could also do:pygame.Rect(left, top, width, height)
                                                         #will use a Sprite Class to combine surface and rectangle later
player_gravity = 0

# Intro screen
player_stand = pygame.image.load('static/images/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand.get_rect(center = (400,200))

game_name = test_font.render('Pixel Runner', False, (111,196,169))
game_name_rect = game_name.get_rect(center = (400,80))

game_message = test_font.render('Press space to run', False, (111,196,169))
game_message_rect = game_message.get_rect(center = (400,320))


# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

while True:
    for event in pygame.event.get(): #checking all events possible and looping through each event
        if event.type == pygame.QUIT: #being able to close the window
            pygame.quit() #quiting pygame
            exit()
    #draw all elements 
    #update everything
        
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN: #MOUSEBUTTONUP/ MOUSEBUTTONDOWN tracks every time you press the button and release it
                if player_rect.collidepoint(event.pos):
                    player_gravity = -20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800
                start_time = int(pygame.time.get_ticks() / 1000)
            
        if event.type == obstacle_timer and game_active:
            obstacle_rect_list.append(snail_surface.get_rect(bottomright = (randint(900, 1100),300)))

    if game_active:
        screen.blit(sky_surface,(0, 0)) #blit= block image transfer (put one surface in another surface) 
                                        #2 arguments (surface, position)
                                        #position = distance from left to right and from top to bottom
        screen.blit(ground_surface,(0, 300))
        # pygame.draw.rect(screen, '#c0e8ec', score_rect) #can use .draw to draw a lot of different things (read documentation)
        # pygame.draw.rect(screen, '#c0e8ec', score_rect, 10) 
        # #pygame.draw.line(screen, 'Gold', (0,0), pygame.mouse.get_pos(), 10) #params: (where you want to draw, color of the line, start point, end point, width of the line)
        # #pygame.mouse.get_pos(): makes the line move acording with the mouse position
        # screen.blit(score_surface,score_rect)
        score = display_score()
        
        # snail_rect.x -= 4
        # screen.blit(snail_surface,snail_rect)
        # if snail_rect.right <= 0:
        #     snail_rect.left = 800 #if the snail desapears from the screen, it appears back on the screen using the screen's width 800 from the top of the coding
                                    #to move the player: player_rect.left += 1
                                    #to know the player's position: print(player_rect.left)
        
        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: #300 because it's the top of the ground
            player_rect.bottom = 300
        screen.blit(player_surf, player_rect)

        # Obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # Collision
        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill((94,129,162))
        screen.blit(player_stand,player_stand_rect)

        score_message = test_font.render(f'Your score: {score}', False, (111,196,169)) 
        score_message_rect = score_message.get_rect(center = (400,330))
        screen.blit(game_name,game_name_rect)

        if score == 0:
            screen.blit(game_message,game_message_rect)
        else:
            screen.blit(score_message, score_message_rect)
        # keys = pygame.key.get_pressed() 
        # if keys[pygame.K_SPACE]:
        #     print('jump')

        # if (player_rect.colliderect(snail_rect)): #print(player_rect.colliderect(snail_rect))->it returns True of False when the player is colliding with the snail or not
        #     print('collision')

        # mouse_position = pygame.mouse.get_pos()
        # if player_rect.collidepoint(mouse_position):
        #     print(pygame.mouse.get_pressed()) #prints True or False when mouse button gets pressed in the position of which button was pressed(right, middle or left button)


    pygame.display.update()
    clock.tick(60) #while loop shouldn't run faster than 60 times per second