import sys
import pygame
from settings_ai import Settings
from ship import Ship
# from peppa import Peppa
from bullet import Bullet
from alien import Alien


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
        self.bullets = pygame.sprite.Group()
        # self.peppa = Peppa(self)
        self.aliens = pygame.sprite.Group()
        self._create_fleet()


    def run_game(self):
        """Start the main loop for the game."""
        
        while True:
            # Watch for keyboard and mouse events.
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

            

            
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            # if event.type == pygame.WINDOWRESIZED: #en cambios del tamaño de la ventana
            #     self.screen.fill(self.settings.bg_color)

            if event.type == pygame.QUIT:
                #pygame.display.quit() --> this quit the windows but the program still running
                sys.exit() # usar este que cierra el programa

            elif event.type == pygame.KEYDOWN: #if key is hold
                self._check_keydown_event(event)
                
            elif event.type == pygame.KEYUP: # if key is released
                self._check_keyup_event(event)

    def _check_keydown_event(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            # Move the ship to the right when the Kright is pressed
            self.ship.moving_right = True
        
        elif event.key == pygame.K_LEFT:
            # move to the left when Kleft is pressed
            self.ship.moving_left = True
        
        elif event.key == pygame.K_q:
            sys.exit()

        elif event.key == pygame.K_SPACE:
            self._fire_bullet()



    def _check_keyup_event(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False



    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()

        
        
        #Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
                print(len(self.bullets))

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.clock.tick(self.settings.fps) # set fps of he windows 
        #print(self.clock.get_fps()) around 39
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # self.peppa.blitme()
        self.aliens.draw(self.screen)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Make the most recently drawn screen visible.
        pygame.display.update() # This will update all the content on the windows same as pygame.display.flip()

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def  _create_fleet(self):
        """Create the fleet of aliens."""
        # Make an alien
        alien = Alien(self)
        self.aliens.add(alien)


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()