import pygame
import random
from pygame.locals import *

pygame.init()

#window variables
WEIDTH = 600
HEIGHT = 600

#colors
bg = (170,130,80 )
body_inner = (50,175,25)
body_outer = (100,100,200)
red = (255,0,0)
food_color = (200,50,140)
red = (255,0,0)

#define fon
font = pygame.font.SysFont(None,35)

#set up rect for play again
again_rect = Rect(WEIDTH//2 -80 , HEIGHT//2 , 150,60)

#create window
window = pygame.display.set_mode((WEIDTH,HEIGHT))
pygame.display.set_caption("Snake")

def draw_screen():
    window.fill(bg)
    #draw grid
    x=0
    y=0
    for i in range(WEIDTH//cell_size):
        x+= cell_size
        y+=cell_size
        pygame.draw.line(window,(255,255,255),(x,0),(x,WEIDTH))
        pygame.draw.line(window,(255,255,255),(0,y),(HEIGHT,y))

def draw_score():
    score_txt = "Score: " + str(score)
    score_img = font.render(score_txt,True,red)
    window.blit(score_img,(0,0))

#game variables
cell_size =10
direction = 1 # 1 for up, 2 for right , 3 for down and 4 for left
update_snake = 0
food = [0,0]
new_food = True
new_piece = [0,0]
score = 0
game_over = False
clicked = False
speed = 25

#creat snake
snake_pos = [[int(WEIDTH/2),int(HEIGHT/2)]]
snake_pos.append([int(WEIDTH/2),int(HEIGHT/2)+ cell_size] )
snake_pos.append([int(WEIDTH/2),int(HEIGHT/2)+ cell_size*2])
snake_pos.append([int(WEIDTH/2),int(HEIGHT/2)+ cell_size*3])

def check_game_over(game_over):
    
    #first chech if snake has eaten itself
    head_count =0
    for segment in snake_pos:
        if snake_pos[0] == segment and head_count > 0:
            game_over = True
        head_count +=1
        
    #chech if snake has gone out of bounds
    if snake_pos[0][0] < 0 or snake_pos[0][0] > WEIDTH or snake_pos[0][1] <0 or snake_pos[0][1] > HEIGHT :
        game_over = True
    return game_over

def draw_game_over():
    over_txt = "Game over!"
    over_img = font.render(over_txt,True,(0,0,255))
    pygame.draw.rect(window,red,(WEIDTH//2 -80 , HEIGHT //2 - 80 , 150 ,60 ))
    window.blit(over_img,(WEIDTH//2 -80 , HEIGHT//2 -60))

    again_txt = "Play Again?"
    again_img = font.render(again_txt,True,(0,0,255))
    pygame.draw.rect(window,red,again_rect)
    window.blit(again_img,(WEIDTH//2 -80 , HEIGHT//2 +15))
    
    


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
    if game_over == False :                
        if update_snake>speed:
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
                
            #check after game upadtes if game is over
            game_over = check_game_over(game_over)
    if game_over == True:
        draw_game_over()
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == True:
            clicked = False
            pos = pygame.mouse.get_pos()

            if again_rect.collidepoint(pos):
                #rest all variables

                direction = 1 # 1 for up, 2 for right , 3 for down and 4 for left
                update_snake = 0
                food = [0,0]
                new_food = True
                new_piece = [0,0]
                score = 0
                game_over = False
                cliked = False

                #creat snake
                snake_pos = [[int(WEIDTH/2),int(HEIGHT/2)]]
                snake_pos.append([int(WEIDTH/2),int(HEIGHT/2)+ cell_size] )
                snake_pos.append([int(WEIDTH/2),int(HEIGHT/2)+ cell_size*2])
                snake_pos.append([int(WEIDTH/2),int(HEIGHT/2)+ cell_size*3])


            
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
