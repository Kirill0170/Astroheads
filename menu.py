import core.log as log
import os,sys

from core.textures import loadBlockTextures

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame,core.textures
from pygame.color import THECOLORS



def menu():
    pygame.init()
    log.prepareNewLog()
    screen = pygame.display.set_mode((800, 600))
    menuState="main"
    textures=loadBlockTextures()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if menuState=="main":
            screen.fill(THECOLORS['black'])
            font = pygame.font.SysFont(None, 40)
            text = font.render(str('HELLO'), True, THECOLORS['green'])
            screen.blit(text,(0,0))
        pygame.display.flip()

if __name__=='__main__':
    try: menu()
    except Exception as e: log.crash(e)