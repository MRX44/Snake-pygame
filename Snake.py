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
food_color = (200,50,140)
score_color = (255,0,0)
#define fon
font = pygame.font.SysFont(None,40)

#create window
window = pygame.display.set_mode((WEIDTH,HEIGHT))
pygame.display.set_caption("Snake")

def draw_screen():
    window.fill(bg)

def draw_score():
    score_txt = "Score: " + str(score)
    score_img = font.render(score_txt,True,score_color)
    window.blit(score_img,(0,0))

#game variables
cell_size =10
direction = 1 # 1 for up, 2 for right , 3 for down and 4 for left
update_snake = 0
food = [0,0]
new_food = True
new_piece = [0,0]
score = 0

#creat snake
snake_pos = [[int(WEIDTH/2),int(HEIGHT/2)]]
snake_pos.append([int(WEIDTH/2),int(HEIGHT/2)+ cell_size] )
snake_pos.append([int(WEIDTH/2),int(HEIGHT/2)+ cell_size*2])
snake_pos.append([int(WEIDTH/2),int(HEIGHT/2)+ cell_size*3])


#set up loop with exit event
run = True

while run:
    draw_screen()
    draw_score()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN :
            if event.key == pygame.K_UP and direction !=3:
                direction = 1
            if event.key == pygame.K_RIGHT and direction !=4:
                direction = 2
            if event.key == pygame.K_DOWN and direction !=1:
                direction = 3
            if event.key == pygame.K_LEFT and direction !=2:
                direction = 4

    if new_food == True :
        new_food = False
        #food cordinates
        food[0] = cell_size * random.randint(0,(WEIDTH / cell_size)-1)
        food[1] = cell_size * random.randint(0,(HEIGHT / cell_size)-1)
        
        
    #draw food
    pygame.draw.rect(window,food_color,(food[0],food[1],cell_size,cell_size))

    #check if food is eaten
    if snake_pos[0] == food :
        new_food = True
        #create new piece at last point at snake's tale
        new_piece = list(snake_pos[-1])

        if direction ==1:
            new_piece[1] += cell_size
        if direction ==3:
            new_piece[1] -= cell_size
        if direction ==2:
            new_piece[0] -= cell_size
        if direction ==4:
            new_piece[0] += cell_size

        #attach new piece
        snake_pos.append(new_piece)

        #update score
        score +=1
                    
    if update_snake>60:
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
