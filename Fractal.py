import pygame
import random
import math
from pygame.math import Vector2
from random import randrange as rr

FRAMERATE = 60
SCREEN_SIZE = Vector2(1000, 1000)

screen = pygame.display.set_mode((SCREEN_SIZE))

def midpoint(x1, x2):
    return ((x1+x2)/2)


    
    
def triangle(x1, y1, x2, y2, x3, y3, counter, isEven):

    counter += 1
    

    if counter > 8:
        return 0
    
    if isEven == 1:
        pygame.draw.polygon(screen, (50, counter/2, rr(0,255)), ((midpoint(x1, x2) , midpoint(y1, y2)) , (midpoint(x2, x3), midpoint(y2, y3)) , (midpoint(x3, x1), midpoint(y3, y1))))


   

    if isEven == -1:
        pygame.draw.polygon(screen, (0,0,0), ((midpoint(x1, x2) , midpoint(y1, y2)) , (midpoint(x2, x3), midpoint(y2, y3)) , (midpoint(x3, x1), midpoint(y3, y1))))
        

    else:
        pygame.draw.polygon(screen, ( rr(0,255),  rr(0,255),  rr(0,255)), ((midpoint(x1, x2), midpoint(y1, y2)), (midpoint(x2, x3), midpoint(y2, y3)), (midpoint(x3, x1), midpoint(y3, y1))))

    pygame.display.flip()
    isEven *= -1

    triangle(x1, y1, midpoint(x1, x2) , midpoint(y1, y2),midpoint(x3, x1), midpoint(y3, y1), counter, isEven)
    
    triangle(x2, y2, midpoint(x1, x2) , midpoint(y1, y2),midpoint(x3, x2) ,midpoint(y3, y2), counter, isEven)

    triangle(x3, y3, midpoint(x2, x3), midpoint(y2, y3),midpoint(x3, x1), midpoint(y3, y1), counter, isEven )


pygame.draw.polygon(screen, ( rr(0,255),  rr(0,255),  rr(0,255)), ((rr(0,1000), rr(0,1000)), (rr(0,1000), rr(0,1000)), (rr(0,1000), rr(0,1000))))




for i in range(0, 5):
    triangle( rr(0,1000), rr(0,1000), rr(0,1000), rr(0,1000), rr(0,1000), rr(0,1000), 0,1)
        
      





while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT: #close game window
        break

pygame.quit()

    