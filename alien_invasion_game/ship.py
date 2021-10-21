import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""

        super().__init__()
        self.screen = ai_game.screen # get Screen (Surface) of the game
        self.screen_rect = ai_game.screen.get_rect() # get a Rect of the entire windows 
        
        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect() # get the rectangle (Rect) of the image
        
        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom # stablish rect of imge ship on the midbotton of the screen
        self.x = float(self.rect.x) # Store a decimal value for the ship's horizontal position.

        # flag for continuos moving to the right (event key hold)
        self.moving_right = False
        self.moving_left = False
        self.settings = ai_game.settings

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right: # limit the movement in the windows only
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed
        # Update rect object from self.x.
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)


    def center_ship(self):
        """Center the ship on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)