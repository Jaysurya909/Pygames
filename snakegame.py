import pygame


#other things
fps=30
clock=pygame.time.Clock()

#colors
white=(255,255,255)
black=(0,0,0)
green=(0,255,0)

#window size
screen_width=700
screen_height=500
gamewindow=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Snake Game")

#Gamevariables
snake_x=45
snake_y=45
snake_size_x=10
snake_size_y=10
snake_velocity_x=5
snake_velocity_y=5
exit_game=False
direction=None


#Gameloop
while not exit_game:
    gamewindow.fill(black)
    pygame.draw.rect(gamewindow,green,[snake_x,snake_y,snake_size_x,snake_size_y])
    
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_game=True

        
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                # snake_x=snake_x+snake_velocity_x
                direction=3     
            if event.key==pygame.K_LEFT:
                # snake_x=snake_x-snake_velocity_x
                direction=4
            if event.key==pygame.K_UP:
                # snake_y=snake_y-snake_velocity_y
                direction=1
            if event.key==pygame.K_DOWN:
                # snake_y=snake_y+snake_velocity_y
                direction=2

    if(direction==1):
        snake_y=snake_y-snake_velocity_y
    elif(direction==2):
        snake_y=snake_y+snake_velocity_y
    elif(direction==3):
        snake_x=snake_x+snake_velocity_x
    elif(direction==4):
        snake_x=snake_x-snake_velocity_x

        



        

    pygame.display.update()




    clock.tick(fps)