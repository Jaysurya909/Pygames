import pygame

gamewindow=pygame.display.set_mode((500,500))
pygame.display.set_caption("New game")
exitgame=False
while not exitgame:
    for event in pygame.event.get():        #you can also write anything else than event
        print(event)
        if event.type==pygame.QUIT:
            exitgame=True

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                print("The right key is pressed")