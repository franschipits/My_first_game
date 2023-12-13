import pygame
from sys import exit

pygame.init() #initializing pygame
screen = pygame.display.set_mode((800, 400)) #args (width, height)
pygame.display.set_caption('My first game')
clock = pygame.time.Clock() #creates a clock object

test_surface = pygame.Surface((100, 200)) #args (width, height)
test_surface.fill('Red') #fill surface with red color

while True:
    for event in pygame.event.get(): #checking all events possible and looping through each event
        if event.type == pygame.QUIT: #being able to close the window
            pygame.quit() #quiting pygame
            exit()
    #draw all elements 
    #update everything

    screen.blit(test_surface, (0,0)) #blit= block image transfer (put one surface in another surface) 
                                     #2 arguments (surface, position)

    pygame.display.update()
    clock.tick(60) #while loop shouldn't run faster than 60 times per second