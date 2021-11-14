import pygame 
import sys#to pass system call

pygame.init()

screen = pygame.display.set_mode((1200, 400))

dino_rect = pygame.Rect(100, 250, 64, 64)
cac_rect = pygame.Rect(1100, 300, 20, 20)
ground_rect = pygame.Rect(0, 330,1200, 2)





while True:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()#it will exit the system process
            

    pygame.draw.rect(screen, (100, 100, 100), dino_rect)
    pygame.draw.rect(screen, (100, 100, 100), cac_rect)
    pygame.draw.rect(screen, (100, 100, 100), ground_rect)
    
    
    pygame.display.update()
    
    
    
    
    
