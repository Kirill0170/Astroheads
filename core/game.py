import pygame,sys
import core.log as log

def main(screen,SIZE):
    SCREEN_WIDTH, SCREEN_HEIGHT= SIZE
    log.log("GAME","Started Game!")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((200, 255, 255))
        pygame.display.flip()