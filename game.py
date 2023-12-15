import pygame
from sys import exit

pygame.init() #initializing pygame
screen = pygame.display.set_mode((800, 400)) #args (width, height)
pygame.display.set_caption('My first game')
clock = pygame.time.Clock() #creates a clock object
test_font = pygame.font.Font('static/font/Pixeltype.ttf', 50) #args (font type, font size)

sky_surface = pygame.image.load('static/images/Sky.png') 
ground_surface = pygame.image.load('static/images/ground.png')
text_surface = test_font.render("My Game", False, 'Black') #args (text, Anti-Aliasing, color) AA = smooth edges

snail_surface = pygame.image.load('static/images/snail1.png')
snail_x_position = 600

while True:
    for event in pygame.event.get(): #checking all events possible and looping through each event
        if event.type == pygame.QUIT: #being able to close the window
            pygame.quit() #quiting pygame
            exit()
    #draw all elements 
    #update everything

    screen.blit(sky_surface,(0, 0)) #blit= block image transfer (put one surface in another surface) 
                                         #2 arguments (surface, position)
                                         #position = distance from left to right and from top to bottom
    screen.blit(ground_surface,(0, 300))
    screen.blit(text_surface,(300, 50))
    snail_x_position -= 4
    screen.blit(snail_surface,(snail_x_position, 250))

    pygame.display.update()
    clock.tick(60) #while loop shouldn't run faster than 60 times per second