import  pygame
import sys


clock= pygame.time.Clock()
fps=120
rozliseni=rozliseni_x,rozliseni_y=1000,500
okno=pygame.display.set_mode(rozliseni)

while True:
    
    
    
    
    
    
    clock.tick(fps)
    for udalost in pygame.event.get():
            if udalost.type == pygame.QUIT :
                pygame.quit()
                sys.exit
    
    pygame.display.update()