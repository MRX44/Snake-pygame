import pygame
import random

pygame.init()

#window variables
WEIDTH = 600
HEIGHT = 600

#colors
bg = (255,200,150)
body_inner = (50,175,25)
body_outer = (100,100,200)
red = (255,0,0)

#create window
window = pygame.display.set_mode((WEIDTH,HEIGHT))
pygame.display.set_caption("Snake")
def draw_screen():
    window.fill(bg)

#game variables
cell_size =10
direction = 1 # 1 for up, 2 for right , 3 for down and 4 for left
update_snake = 0

#creat snake
snake_pos = [[int(WEIDTH/2),int(HEIGHT/2)]]
snake_pos.append([int(WEIDTH/2),int(HEIGHT/2)+ cell_size] )
snake_pos.append([int(WEIDTH/2),int(HEIGHT/2)+ cell_size*2])
snake_pos.append([int(WEIDTH/2),int(HEIGHT/2)+ cell_size*3])


#set up loop with exit event
run = True

while run:
    draw_screen()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN and direction !=3:
            if event.key == pygame.K_UP:
                direction = 1
            if event.key == pygame.K_RIGHT and direction !=4:
                direction = 2
            if event.key == pygame.K_DOWN and direction !=1:
                direction = 3
            if event.key == pygame.K_LEFT and direction !=2:
                direction = 4
    if update_snake>99:
        update_snake =0
        
        snake_pos = snake_pos[-1:] + snake_pos[:-1]
        if direction == 1:
            snake_pos[0][0] = snake_pos[1][0]
            snake_pos[0][1] = snake_pos[1][1] - cell_size
        if direction == 3:
            snake_pos[0][0] = snake_pos[1][0]
            snake_pos[0][1] = snake_pos[1][1] + cell_size
        if direction == 2:
            snake_pos[0][0] = snake_pos[1][0] + cell_size
            snake_pos[0][1] = snake_pos[1][1] 
        if direction == 4:
            snake_pos[0][0] = snake_pos[1][0] - cell_size
            snake_pos[0][1] = snake_pos[1][1] 
    
            
    #draw snake
    head = 1
    for x in snake_pos:
        if head==0:
            pygame.draw.rect(window,body_outer,(x[0],x[1],cell_size,cell_size))
            pygame.draw.rect(window,body_inner,(x[0]+1,x[1]+1,cell_size-2,cell_size-2))
        if head ==1:
            pygame.draw.rect(window,body_outer,(x[0],x[1],cell_size,cell_size))
            pygame.draw.rect(window,red,(x[0]+1,x[1]+1,cell_size-2,cell_size-2))
            head=0
        
    #update the display
    pygame.display.update()
    update_snake+=1


pygame.quit()
