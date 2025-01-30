import pygame

class Rocket:
    """A class to manage the rocket"""

    def __init__(self, r_game):
        self.screen = r_game.screen
        self.settin = r_game.settin
        self.screen_rect = r_game.screen.get_rect()

        #Load the rocket image and get its rect

        self.image = pygame.image.load('rocket.bmp')
        self.rect = self.image.get_rect()

        #start each new rocket at the center of the screen.
        self.rect.center = self.screen_rect.center

        #Store a decimal value for the rockets horizontal
        #and vertical position

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        #movement flags
        self.moving_right, self.moving_left = False, False
        self.moving_up , self.moving_down = False, False
    
    def update(self):
        """Update the rockets position basedon  movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settin.rocket_speed
        if self.moving_left and self.rect.left >0:
            self.x -=self.settin.rocket_speed
        if self.moving_up and self.rect.top >0:
            self.y -=self.settin.rocket_speed
        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.y += self.settin.rocket_speed

            #update the rect object from positon

        self.rect.x =self.x
        self.rect.y= self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)
    