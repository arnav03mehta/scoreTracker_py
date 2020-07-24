import PyGressBar 
import pygame
import sys

pygame.init()
res = (1080,720) 
screen = pygame.display.set_mode(res) 

running = True
while running :

    for event in pygame.event.get() :

        if event == pygame.QUIT :
            running = False

    PyGressBar.bar()

