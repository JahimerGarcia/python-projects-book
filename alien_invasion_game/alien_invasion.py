import sys
import pygame
from settings_ai import Settings
from ship import Ship
from peppa import Peppa


class AlienInvasion:
    """ 
    Overall class to manage game assets and behavior.
    """
    def __init__(self):
        """
        Initialize the game, and create game resources.
        """
        pygame.init()
        self.settings = Settings() # this is a class module with all settings
        # start the windows and set the size, you can use | (pipe) to pass more flags
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height), flags= pygame.RESIZABLE | pygame.SCALED) 
        pygame.display.set_caption("Alien Invasion") # name of the windows appear above 
        self.ship = Ship(self)
          # this will be used for fps
        self.clock = pygame.time.Clock()
        self.peppa = Peppa(self)

    def run_game(self):
        """Start the main loop for the game."""
        
        while True:
            self._update_screen()
            # Watch for keyboard and mouse events.
            self._check_events()
            
        # Make the most recently drawn screen visible.
            pygame.display.update() # This will update all the content on the windows same as pygame.display.flip()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            # if event.type == pygame.WINDOWRESIZED: #en cambios del tamaño de la ventana
            #     self.screen.fill(self.settings.bg_color)

            if event.type == pygame.QUIT:
                #pygame.display.quit() --> this quit the windows but the program still running
                sys.exit() # usar este que cierra el programa y 

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.clock.tick(self.settings.fps) # set fps of he windows 
        #print(self.clock.get_fps()) around 39
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # Make the most recently drawn screen visible.
        pygame.display.update() # This will update all the content on the windows same as pygame.display.flip()
        self.peppa.blitme()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()