import os
import pygame,sys
import core.log as log
from core.blocks.blocks import loadBlocks
from core.textures import loadBlockTextures
def main(screen,SIZE):
    SCREEN_WIDTH, SCREEN_HEIGHT= SIZE
    block_textures=loadBlockTextures()
    blocks=loadBlocks(os.path.join('core','blocks','blocksdir'))
    log.log("GAME","Started block test")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((200, 255, 255))
        x=0
        for name,block in blocks.items():
            block=block()
            screen.blit(block_textures[block.textureName],(x,0))
            x+=32
        pygame.display.flip()