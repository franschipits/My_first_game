import pygame
from sys import exit

pygame.init() #initializing pygame
screen = pygame.display.set_mode((800, 400)) #args (width, height)
pygame.display.set_caption('My first game')
clock = pygame.time.Clock() #creates a clock object
test_font = pygame.font.Font('static/font/Pixeltype.ttf', 50) #args (font type, font size)
game_active = True


sky_surface = pygame.image.load('static/images/Sky.png').convert() #.convert=it converts to a type of image pygame can work with more easily and makes the game run faster
ground_surface = pygame.image.load('static/images/ground.png').convert()

score_surface = test_font.render("My Game", False, (64,64,64)) #args (text, Anti-Aliasing, color) AA = smooth edges
score_rect = score_surface.get_rect(center = (400, 50)) #400 is half of width of screen so it's in the middle and 50 is what we used screen.blit(score_surface, (300,50)) down bellow before

snail_surface = pygame.image.load('static/images/snail1.png').convert_alpha() #removing alpha values
#snail_x_position = 600
snail_rect = snail_surface.get_rect(bottomright = (600,300))

player_surf = pygame.image.load('static/images/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300)) #(topleft=(x,y))
                                                        #could also do:pygame.Rect(left, top, width, height)
                                                        #will use a Sprite Class to combine surface and rectangle later
player_gravity = 0

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

    if game_active:
        screen.blit(sky_surface,(0, 0)) #blit= block image transfer (put one surface in another surface) 
                                            #2 arguments (surface, position)
                                            #position = distance from left to right and from top to bottom
        screen.blit(ground_surface,(0, 300))
        pygame.draw.rect(screen, '#c0e8ec', score_rect) #can use .draw to draw a lot of different things (read documentation)
        pygame.draw.rect(screen, '#c0e8ec', score_rect, 10) 
        #pygame.draw.line(screen, 'Gold', (0,0), pygame.mouse.get_pos(), 10) #params: (where you want to draw, color of the line, start point, end point, width of the line)
        #pygame.mouse.get_pos(): makes the line move acording with the mouse position
        screen.blit(score_surface,score_rect)
        # snail_x_position -= 4
        # if snail_x_position < -100:
        #     snail_x_position = 800
        snail_rect.x -= 4
        screen.blit(snail_surface,snail_rect)
        if snail_rect.right <= 0:
            snail_rect.left = 800 #if the snail desapears from the screen, it appears back on the screen using the screen's width 800 from the top of the coding
        #to move the player: player_rect.left += 1
        #to know the player's position: print(player_rect.left)
        
        #Player:
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: #300 because it's the top of the ground
            player_rect.bottom = 300
        screen.blit(player_surf, player_rect)

        #collision
        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill('Yellow')

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