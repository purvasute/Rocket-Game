import sys

import pygame

from settin import Settin
from rocket import Rocket

class RocketGame:
    """Overall class to manage game assets and behavior."""
    def __init__(self):
        """Initialize the game and create a game resource."""
        pygame.init()
        
        self.settin = Settin()
        self.screen = pygame.display.set_mode(
            (self.settin.screen_width, self.settin.screen_height))
        pygame.display.set_caption("Rocket Game")
        self.rocket = Rocket(self)

    def run_game(self):
        """Initialize the main loop for the game."""
        while True:
            self._check_events()
            self.rocket.update()
            self._update_screen()


    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type ==pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keydown"""
        if event.key ==pygame.K_RIGHT:
            self.rocket.moving_right =True
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = True
        if event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key ==pygame.K_DOWN:
            self.rocket.moving_down =True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to keyup. """
        if event.key ==pygame.K_RIGHT:
            self.rocket.moving_right =False
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
        if event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key ==pygame.K_DOWN:
            self.rocket.moving_down =False
        
    
    def _update_screen(self):
        """Update the image on the screen and flip to the new screen."""
        self.screen.fill(self.settin.bg_color)
        self.rocket.blitme()

        pygame.display.flip()

if __name__== '__main__':
    #make a game instance and run the game.
    rg = RocketGame()
    rg.run_game()

        

