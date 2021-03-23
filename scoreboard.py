import pygame


class Scoreboard:
    """a class to show score"""
    def __init__(self, ai_settings, stats, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        self.text_color = (200, 200, 200)
        self.font = pygame.font.Font('fonts/numbers.ttf', 40)
        self.font2 = pygame.font.Font('fonts/numbers.ttf', 30)

        # ships left stuff
        self.image = pygame.image.load('images/ship0.bmp')
        self.image = pygame.transform.scale(self.image, ai_settings.ship_icon_size)
        self.ship_icon_rect = self.image.get_rect()
        self.ship_icon_rect.top = 20

        self.prep_score()

    def prep_score(self):
        """turn the score into an image"""
        score_str = self.ai_settings.dictionary['score'] + ': ' + str(int(self.stats.score))
        self.score_image = self.font.render(score_str, True, self.text_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = self.screen_rect.left + 20
        self.score_rect.top = self.screen_rect.top + 20

        # same for level
        level_str = self.ai_settings.dictionary['level'] + ': ' + str(int(self.stats.level))
        self.level_image = self.font2.render(level_str, True, self.text_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.screen_rect.left + 20
        self.level_rect.top = self.screen_rect.top + self.score_rect.height + 30

        # same for high score
        high_score_str = self.ai_settings.dictionary['high score'] + ': ' + str(int(self.stats.high_score))
        self.high_score_image = self.font2.render(high_score_str, True, self.text_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.left = self.screen_rect.left + 20
        self.high_score_rect.top = self.screen_rect.top + self.score_rect.height + self.level_rect.height + 40

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)

        drawn = 0
        for ship in range(self.stats.ships_left):
            self.ship_icon_rect.right = self.screen_rect.right - 20 - drawn * (10 + self.ship_icon_rect.width)
            self.screen.blit(self.image, self.ship_icon_rect)
            drawn += 1
