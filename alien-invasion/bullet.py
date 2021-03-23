import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets flying from the ship"""

    def __init__(self, ai_settings, screen, ship):
        """create a bullet from the ship's current location"""
        super().__init__()
        self.screen = screen

        # create a bullet rectangle at (0, 0) and then set the correct position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # a float for bullets position
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed = ai_settings.bullet_speed

    def update(self):
        """updates the bullet's position"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
