import sys
import pygame



class AlienInvasion:
    """ 
    Overall class to manage game assets and behavior.
    """
    def __init__(self):
        """
        Initialize the game, and create game resources.
        """
        
        pygame.init()
        self.screen = pygame.display.set_mode((500,500), flags= pygame.RESIZABLE | pygame.SCALED) # start the windows and set the size, you can use | (pipe) to pass more flags 
        pygame.display.set_caption("Alien Invasion") # name of the windows appear above 

    def run_game(self):
        """Start the main loop for the game."""
        self.clock = pygame.time.Clock()  # this will be used for fps

        while True:
            self.clock.tick(40) # set fps of he windows 
            # print(self.clock.get_fps()) around 39 fps
            
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    #pygame.display.quit() --> this quit the windows but the program still running
                    sys.exit() # usar este que cierra el programa y 
        
        # Make the most recently drawn screen visible.
            pygame.display.update() # This will update all the content on the windows same as pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()