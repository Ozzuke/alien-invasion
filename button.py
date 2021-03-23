import pygame.font


class Button:
    """a class for a button"""
    def __init__(self, ai_settings, screen):
        """initialize the button's attributes"""
        self.ai_settings = ai_settings
        self.screen = screen
        self.msg = ai_settings.dictionary['play']
        self.screen_rect = screen.get_rect()

        # set the dimensions and properties of the button
        self.width, self.height = 300, 150
        self.button_color = (128, 0, 255)
        self.width2, self.height2 = 320, 170
        self.button_color2 = (90, 0, 255)
        self.text_color = (0, 0, 0)
        self.font_path = self.ai_settings.font_path
        self.font = pygame.font.Font(self.font_path, 60)

        # build the button's rect object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.rect2 = pygame.Rect(0, 0, self.width2, self.height2)
        self.rect2.center = self.screen_rect.center

        # the message on the button needs to be prepped
        self.prep_msg(self.msg)

    def prep_msg(self, msg):
        """turns msg into a rendered image and center text on the button"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # draw blank button and then draw message
        self.screen.fill(self.button_color2, self.rect2)
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
