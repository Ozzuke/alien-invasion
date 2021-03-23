import pygame
from pygame.sprite import Sprite
from random import randint


class Alien(Sprite):
    """a class for aliens in the game"""

    def __init__(self, ai_settings, screen, stats):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # load an image of an alien
        self.image = pygame.image.load(f'images/alien'
            f'{str(0 if not stats.created else stats.level if stats.level < 4 else randint(0, 3))}.bmp')
        self.image = pygame.transform.scale(self.image, self.ai_settings.alien_size)
        self.rect = self.image.get_rect()

        # start each alien in the upper left corner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the aliens exact position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    # make the alien visible
    def blitme(self):
        """draw the alien in it's current location"""
        self.screen.blit(self.image, self.rect)

    def update(self, ship, aliens):
        self.x += self.ai_settings.alien_speed * self.ai_settings.fleet_direction
        self.rect.x = self.x

    def check_edge(self):
        """return True if alien is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= screen_rect.left:
            return True
