import pygame
from pygame.sprite import Sprite
from random import randint


class Star(Sprite):
    """creates stars for background"""

    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('images/star.bmp')
        self.image = pygame.transform.scale(self.image, [10, 8])
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.x = 0

    def update(self):
        """update the star to move"""
        self.x += 0.1
        self.rect.centerx = self.x

        if self.rect.left >= self.screen_rect.right:
            self.x -= self.screen_rect.width + self.rect.width
            self.rect.y = randint(0, self.screen_rect.height)

    def blitme(self):
        """draw the star on the screen"""
        self.screen.blit(self.image, self.rect)


class Planet(Sprite):
    """creates stars for background"""

    def __init__(self, screen, image_numbers):
        super().__init__()
        self.screen = screen
        self.planet_speed = 0.3

        # creates a random planet image from selection
        self.image_prefix = 'images/planet_'
        self.image_addition = '.bmp'
        image_numbers_len = len(image_numbers)
        image_number = randint(1, image_numbers_len) - 1
        self.stored_image_number = image_numbers.pop(image_number)
        self.image_path = self.image_prefix + self.stored_image_number + self.image_addition

        self.image = pygame.image.load(self.image_path)
        self.image_size = randint(20, 50)
        if self.image_path == 'images/planet_0.bmp':
            self.image = pygame.transform.scale(self.image, [self.image_size * 3, self.image_size * 3])
        else:
            self.image = pygame.transform.scale(self.image, [self.image_size, self.image_size])

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.x = 0

    def update(self, image_numbers):
        """update the planet to move"""
        self.x += self.planet_speed
        self.rect.right = self.x

        if self.rect.left - 100 >= self.screen_rect.right:
            # death star easter egg
            if randint(1, 10) == 10:
                self.image = pygame.image.load('images/death_star.bmp')
                self.image = pygame.transform.scale(self.image, [500, 500])
            else:
                # creates a random planet image from selection
                image_numbers.append(self.stored_image_number)
                image_numbers_len = len(image_numbers)
                image_number = randint(1, image_numbers_len) - 1
                self.stored_image_number = image_numbers.pop(image_number)
                self.image_path = self.image_prefix + self.stored_image_number + self.image_addition

                self.image = pygame.image.load(self.image_path)
                self.image_size = randint(20, 50)
                if self.image_path == 'images/planet_0.bmp':
                    self.image = pygame.transform.scale(self.image, [self.image_size * 3, self.image_size * 3])
                else:
                    self.image = pygame.transform.scale(self.image, [self.image_size, self.image_size])

            self.x -= self.screen_rect.width + self.rect.width + randint(150, 3000)
            self.rect.y = randint(self.rect.height, self.screen_rect.height - self.rect.height)

    def blitme(self):
        """draw the star on the screen"""
        self.screen.blit(self.image, self.rect)