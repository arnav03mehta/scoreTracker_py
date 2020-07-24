import pygame
import sys,json
from main_modules import add,show,reset

pygame.init()
res = (1080,720) 
screen = pygame.display.set_mode(res) 

smallfont = pygame.font.SysFont('Times New Roman',40) 

button = (40,50)
r = pygame.Rect(button,(190,50))
reset_button = pygame.Rect((40,110),(50,50))
q = [2,1]
running = True

while running : 

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT: 
            running = False

        if ev.type == pygame.KEYDOWN :
            if ev.key == pygame.K_ESCAPE :
                running = False

        if ev.type == pygame.MOUSEBUTTONDOWN :
			
            if r[0] <= mouse[0] <= r[0]+190 and r[1] <= mouse[1] <= r[1]+50: 
                add(*q)

            elif 40 <= mouse[0] <= 90 and 110 <= mouse[1] <= 160: 
                reset(*q)

    text = smallfont.render(f"clicks : {show(*q)}" ,True,(0,0,255))

    mouse = pygame.mouse.get_pos()

    if r[0] <= mouse[0] <= r[0]+190 and r[1] <= mouse[1] <= r[1]+50: 
        
        pygame.draw.rect(screen,(120,120,0),r)

    elif 40 <= mouse[0] <= 90 and 110 <= mouse[1] <= 160: 
        
        pygame.draw.rect(screen,(255,0,0),reset_button)

    else : 
        
        pygame.draw.rect(screen,(255,255,255),r)
        
        pygame.draw.rect(screen,(255,255,255),pygame.Rect((40,110),(50,50)))

    screen.blit(text,(button[0]+6,button[1]+1))

    pygame.display.update()
