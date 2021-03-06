import pygame
import random

pygame.init()

#window variables
WEIDTH = 600
HEIGHT = 600

#create window
window = pygame.display.set_mode((WEIDTH,HEIGHT))
pygame.display.set_caption("Snake")
window.fill((255,200,150))


#set up loop with exit event
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False




    #update the display
    pygame.display.update()


pygame.quit()
