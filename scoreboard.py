import pygame.font
from pygame.sprite import Group
from ship import Life


class Scoreboard:
    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_level(self):
        """Draw current level"""
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.ai_settings.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom

    def prep_high_score(self):
        """Top score at the middle"""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "High Score: {:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_score(self):
        """Current score shows at top right"""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "Score: {:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 0

    def show_score(self):
        """Draw score to the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        """Draw ships as remaining lives"""
        self.ships.draw(self.screen)

    def prep_ships(self):
        """Draw remaining lives"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Life(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * (ship.rect.width + 10)
            ship.rect.y = 0
            self.ships.add(ship)