"""
    Voltes V Crewzer Game
    Raymond Hernandez
    October 17, 2020

"""
import pygame
import game_functions as gf
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship


def run_game():
    """ Initialize Pygame """
    pygame.init()

    """ Initializes the screen """
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height), pygame.FULLSCREEN)
    pygame.display.set_caption("Voltes V Crewzer")

    """ Game Variables """
    play_button = Button(ai_settings, screen, "Play Game")
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    """ Prepare the alien fleet """
    gf.create_fleet(ai_settings, screen, ship, aliens)

    """ Game's main loop """
    while True:
        """ Listens to any change in sprite (alien, ship, bullets) locations or scores """
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            """ Moves the ship left or right """
            ship.update()

            """ Deletes bullets past screen, to avoid slowing the game """
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)

            """ Check destroyed aliens, collision with ship or past the bottom screen """
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        """ Blits screen """
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

""" Makes sure run_game() is ran first on other compilers """
if __name__ == "__main__":
    run_game()