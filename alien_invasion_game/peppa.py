import pygame

class Peppa():
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen # get Screen (Surface) of the game
        self.screen_rect = ai_game.screen.get_rect() # get a Rect of the entire windows 
        
        # Load the ship image and get its rect.
        self.image = pygame.image.load('images\peppa-767x1024 (1).png')
        self.rect = self.image.get_rect() # get the rectangle (Rect) of the image
        
        # Start each new ship at the bottom center of the screen.
        self.rect.center = self.screen_rect.center # stablish rect of imge ship on the midbotton of the screen

    
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)