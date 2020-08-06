import sys

import pygame

class AlienInvasion:
    """overall class to manage game assets and behavior."""

    def __init__(self):
        """initialize the game and create game resources"""
        pygame.init()

        self.screen=pygame.display.set_mode((1200,800))
        pygame.display.set_caption("alien invasion")
        self.bg_color=(230,230,230)

    def run_game(self):
        """start the main loop for the game"""
        while True:
            #watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()

            #redraw ehte screen during each pass through the loop:
            self.screen.fill(self.bg_color)
            #make the most recently drawn screen visible:
            pygame.display.flip()

if __name__ == '__main__':
    #make a game instance, and run the game
    ai=AlienInvasion()
    ai.run_game()
