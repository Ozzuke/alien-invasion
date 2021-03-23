import pygame


class Ship:
    """the player ship class"""

    def __init__(self, screen, ai_settings):
        """initialise the ship and set it's starting position"""
        self.screen = screen
        self.ai_settings = ai_settings

        # load self image
        self.image = pygame.image.load('images/ship0.bmp')
        self.image = pygame.transform.scale(self.image, self.ai_settings.ship_size)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.ship_image_number = 0
        self.frame_counter = 0

        # start each new ship from the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # create a float variable to store ship position
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # create movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.moving_speed = self.ai_settings.ship_speed

    def blitme(self):
        """draw the ship at it's current location"""
        self.change_ship()
        self.image = pygame.transform.scale(self.image, self.ai_settings.ship_size)
        self.screen.blit(self.image, self.rect)

    def update(self):
        # move the ship
        self.move_ship()

        # update center position
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def change_ship(self):
        ship_path_start = 'images/ship'
        self.image = pygame.image.load(ship_path_start + str(self.ship_image_number) + '.bmp')
        if self.frame_counter == self.ai_settings.change_frame_speed:
            if self.ship_image_number < 2:
                self.ship_image_number += 1
            else:
                self.ship_image_number = 0
            self.frame_counter = 0
        self.frame_counter += 1

    def move_ship(self):
        """moves the ship as necessary if it is not at an edge"""
        if self.moving_left and self.rect.left - 10 > self.screen_rect.left:
            self.centerx -= self.ai_settings.ship_speed

        if self.moving_right and self.rect.right + 10 < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed

        if self.moving_up and self.rect.top - 10 > self.screen_rect.top:
            self.centery -= self.ai_settings.ship_speed

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed

    def center_ship(self):
        self.centerx = self.screen_rect.centerx