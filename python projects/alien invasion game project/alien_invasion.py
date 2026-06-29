import sys
import pygame
from settings import Settings
from ship import Ship



def run_game():
    pygame.init()
    alien_invasion_settings = Settings()
    screen = pygame.display.set_mode(
        (alien_invasion_settings.screen_width,alien_invasion_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')


    #create player ship
    ship = Ship(screen)

    #loop for game
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


        #redraw screen during each loop pass
        screen.fill(alien_invasion_settings.bg_color)
        ship.blitme()

        # visualise most recently drawn frame
        pygame.display.flip()


run_game()


