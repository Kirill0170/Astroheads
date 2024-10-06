from tornado.gen import sleep

import core.log as log
import os,sys,time

from core.textures import loadBlockTextures

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame,core.textures
from pygame.color import THECOLORS

pygame.init()
log.prepareNewLog()
SCREEN_WIDTH=800
SCREEN_HEIGHT=600
MENU_DELAY = 0.2
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Astroheads")

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 74)
        self.selected_option = 0
        self.last_input_time = time.time()
        self.mainOptions=["Start Game", "Instructions", "Exit"]

    def draw(self,type="main"):
        self.screen.fill(THECOLORS['black'])
        if type=="main":
            for index, option in enumerate(self.mainOptions):
                color = (255, 0, 0) if index == self.selected_option else (255, 255, 255)
                text = self.font.render(option, True, color)
                text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + index * 100))
                self.screen.blit(text, text_rect)
        pygame.display.flip()

    def handle_input(self):
        current_time = time.time()
        keys = pygame.key.get_pressed()

        # Check if the delay has passed since the last input
        if current_time - self.last_input_time >= MENU_DELAY:
            if keys[pygame.K_UP]:
                self.selected_option = (self.selected_option - 1) % len(self.mainOptions)
                self.last_input_time = current_time  # Update the last input time
            elif keys[pygame.K_DOWN]:
                self.selected_option = (self.selected_option + 1) % len(self.mainOptions)
                self.last_input_time = current_time  # Update the last input time
            elif keys[pygame.K_RETURN]:
                if self.selected_option == 0:
                    return "start_game"
                elif self.selected_option == 1:
                    return "instructions"
                elif self.selected_option == 2:
                    pygame.quit()
                    sys.exit()
        return "menu"
    def drawHelp(self):
        text = self.font.render("help menu", True, THECOLORS["white"])
        self.screen.blit(text, (0,0))
        pygame.display.flip()

def menu():
    menu = Menu(screen)
    game_active = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if not game_active:
            menu.draw()
            action = menu.handle_input()
            if action == "start_game":
                game_active = True
            elif action == "instructions":
                menu.drawHelp()
        else:
            # Game logic goes here
            break
    from core.game import main
    main(screen,(SCREEN_WIDTH,SCREEN_HEIGHT))

if __name__=='__main__':
    try: menu()
    except Exception as e: log.crash(e)