import pygame

#colors
white=(255,255,255)
black=(0,0,0)

#window size
screen_width=700
screen_height=500
gamewindow=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Snake Game")

#Gamevariables
exit_game=False

#Gameloop
while not exit_game:
    gamewindow.fill(white)
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_game=True
