import pygame


class Languages:
    def __init__(self):
        self.eng = {'play': 'play', 'game over': 'GAME OVER!', 'r to restart': 'Press R to restart, Q to quit.',
                    'score': 'Score', 'high score': 'High score', 'version': 'Version', 'level': 'Level'}
        self.est = {'play': 'Alusta', 'game over': 'Kogu lugu!', 'r to restart': 'Uuesti alustamiseks vajutage R, '
                                                                                'lahkumiseks Q.',
                    'score': 'Skoor', 'high score': 'Kõrgeim tulemus', 'version': 'Versioon', 'level': 'Tase'}


class EngButton:
    """a class for a button"""
    def __init__(self, ai_settings, screen):
        """initialize the button's attributes"""
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load(f'images/eng_flag.bmp')
        self.image = pygame.transform.scale(self.image, self.ai_settings.flag_size)
        self.rect = self.image.get_rect()

        # set the flag's position
        self.rect.center = ((self.screen_rect.right - 30 - self.ai_settings.flag_size[0] / 2),
                             (self.screen_rect.top + 30 + self.ai_settings.flag_size[1] / 2))

        # create the highlight for the button
        self.width, self.height = self.rect.width + 8, self.rect.height + 8
        self.color = (50, 50, 50)
        self.highlight_rect = pygame.Rect(0, 0, self.width, self.height)
        self.highlight_rect.center = self.rect.center

    def blitme(self):
        self.screen.fill(self.color, self.highlight_rect)
        self.screen.blit(self.image, self.rect)


class EstButton:
    """a class for a button"""

    def __init__(self, ai_settings, screen):
        """initialize the button's attributes"""
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load(f'images/est_flag.bmp')
        self.image = pygame.transform.scale(self.image, self.ai_settings.flag_size)
        self.rect = self.image.get_rect()

        # set the flag's position
        self.rect.center = ((self.screen_rect.right - 30 - self.ai_settings.flag_size[0] / 2),
                            (self.screen_rect.top + 2 * 30 + 3 * self.ai_settings.flag_size[1] / 2))

        # create the highlight for the button
        self.width, self.height = self.rect.width + 8, self.rect.height + 8
        self.color = (50, 50, 50)
        self.highlight_rect = pygame.Rect(0, 0, self.width, self.height)
        self.highlight_rect.center = self.rect.center

    def blitme(self):
        self.screen.fill(self.color, self.highlight_rect)
        self.screen.blit(self.image, self.rect)
