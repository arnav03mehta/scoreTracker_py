import pygame
import sys,json
from main_modules import add,show,reset_all,progress

pygame.init()
res = (1080,720) 
screen = pygame.display.set_mode(res) 
#bg = pygame.image.load("nack.jpg").convert()
white = (255,255,255)
highlight = (200,200,200)
yelllow_ish = (173,216,230)

the_font = pygame.font.SysFont('Times New Roman',48)
other_font = pygame.font.SysFont('Times New Roman',40)
italic_font = pygame.font.SysFont('Segoe UI',20)

buttons = [(95,130),(325,130),(555,130),(785,130),
        (95,230),(325,230),(555,230),(785,230),
        (95,330),(325,330),(555,330),(785,330),
        (95,430)]

dim = (210,70)
hover = pygame.Surface(dim, pygame.SRCALPHA)   
hover.fill((100,100,100,90))       


def main_buttons() :

    screen.fill(white)
    mouse = pygame.mouse.get_pos()

    for i in range(13) :

        if buttons[i][0] <= mouse[0] <= buttons[i][0]+210 and buttons[i][1] <= mouse[1] <= buttons[i][1]+70 :
            
            #pygame.draw.rect(screen,highlight,pygame.Rect(buttons[i],dim))
            screen.blit(hover,buttons[i])

        else : 
            pygame.draw.rect(screen,yelllow_ish,pygame.Rect(buttons[i],dim))

        text = the_font.render(f"Chapter{i+1}" ,True, (0,0,0))
        screen.blit(text,(buttons[i][0]+6,buttons[i][1]+9))


def Chapter(ch) :

    exercises = [5, 3, 5, 7, 9, 6, 12, 3, 7, 5, 4, 3, 6]

    Ch1_surface = pygame.Surface((1080,720))
    Ch1_surface.fill(white)
    screen.blit(Ch1_surface,(0,0))
    

    for i in range(exercises[ch-1]) :

        if buttons[i][0] <= mouse[0] <= buttons[i][0]+210 and buttons[i][1] <= mouse[1] <= buttons[i][1]+70 :
            
            screen.blit(hover,buttons[i])

        else : 
            pygame.draw.rect(screen,yelllow_ish,pygame.Rect(buttons[i],dim))

        text = other_font.render(f"ex{i+1} ({show(screen_on,i+1)})" ,True, (0,0,0))
        screen.blit(text,(buttons[i][0]+6,buttons[i][1]+9))


def b_r() :

    back_buttons = [(95,590),(325,590)]

    for i in range(2) :
        
        if back_buttons[i][0] <= mouse[0] <= back_buttons[i][0]+210 and back_buttons[i][1] <= mouse[1] <= back_buttons[i][1]+70 :
                
                screen.blit(hover,back_buttons[i])

        else : 
                pygame.draw.rect(screen,yelllow_ish,pygame.Rect(back_buttons[i],dim))

        if i == 0 :
            text = other_font.render(f"back" ,True, (0,0,0))
            screen.blit(text,(back_buttons[i][0]+6,back_buttons[i][1]+9))
        else : 
            text = other_font.render(f"reset" ,True, (0,0,0))
            screen.blit(text,(back_buttons[i][0]+6,back_buttons[i][1]+9))



back_buttons = [(95,590),(325,590)]
screen_on = 0
exercises = [5, 3, 5, 7, 9, 6, 12, 3, 7, 5, 4, 3, 6]

running = True
while running : 

    mouse = pygame.mouse.get_pos()

    for ev in pygame.event.get():

        if ev.type == pygame.QUIT: 
            running = False
    
        if ev.type == pygame.KEYDOWN :
            
            if ev.key == pygame.K_ESCAPE :
                screen_on = 0
        
        if ev.type == pygame.MOUSEBUTTONDOWN :
            for i in range(13) :

                if buttons[i][0] <= mouse[0] <= buttons[i][0]+210 and buttons[i][1] <= mouse[1] <= buttons[i][1]+70 :
                    
                    if screen_on == 0 :
                        screen_on = i+1
                    
                    elif screen_on > 0 and i < exercises[screen_on-1] :
                        add(screen_on,i+1)
            for i in range(2) :
        
                if back_buttons[i][0] <= mouse[0] <= back_buttons[i][0]+210 and back_buttons[i][1] <= mouse[1] <= back_buttons[i][1]+70 :
                    
                    if i == 0 :
                        screen_on = 0 
                    else :
                        reset_all(screen_on)
                        pygame.display.update()


    if screen_on == 0 :
        main_buttons()
    else :
        Chapter(screen_on)
        b_r()
        ch_text = other_font.render(f"Chapter{screen_on}" ,True, (0,0,0))
        screen.blit(ch_text,(820,600))

    pygame.draw.rect(screen,(0,0,0),pygame.Rect((0,0),(1080,720)),30)

    pro_text = italic_font.render(f"Progress" ,True, white)



    pygame.draw.rect(screen,(50,50,50),pygame.Rect((98,53),(progress(),34)))
    pygame.draw.rect(screen,(0,0,0),pygame.Rect((95,50),(900,40)),3)
    screen.blit(pro_text,(105,56))

    pygame.display.update()
