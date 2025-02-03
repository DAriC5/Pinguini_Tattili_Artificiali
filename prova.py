import pygame 

pygame.init()
screen = pygame.display.set_mode((1370, 690))
sfondo = pygame.image.load("img/spazio.png")
sfondo = pygame.transform.scale(sfondo, (screen.get_width(), screen.get_height()))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(sfondo, (0, 0))
    pygame.display.update()