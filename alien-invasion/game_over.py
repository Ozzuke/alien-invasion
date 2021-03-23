import pygame


class GameOver:
    def __init__(self, screen, ai_settings):
        """create the game over message"""
        self.ai_settings = ai_settings
        self.msg = ai_settings.dictionary['game over']
        self.text_color = (128, 0, 255)
        self.font_path = self.ai_settings.font_path
        self.font = pygame.font.Font(self.font_path, 200)
        self.msg_image = self.font.render(self.msg, True, self.text_color)

        # use image instead of text?
        # self.image = pygame.image.load('images/game_over.bmp')
        self.rect = self.msg_image.get_rect()
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        # self.image2 = pygame.image.load('images/r_to_restart.bmp')
        self.msg2 = ai_settings.dictionary['r to restart']
        self.font = pygame.font.Font(self.font_path, 30)
        self.msg_image2 = self.font.render(self.msg2, True, self.text_color)
        self.rect2 = self.msg_image.get_rect()
        self.frames = 0

        self.rect2.centerx = self.screen_rect.centerx
        self.rect2.centery = self.screen_rect.centery + self.rect.height

    def blitme(self):
        self.screen.blit(self.msg_image, self.rect)
        if self.frames < 150:
            self.screen.blit(self.msg_image2, self.rect2)
        if self.frames > 300:
            self.frames = 0
        self.frames += 1