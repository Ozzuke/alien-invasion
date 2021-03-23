import json


class Settings:
    """a class for settings for the game"""
    def __init__(self, languages):
        """initializes the games settings"""
        try:
            with open('data.json', 'r') as file:
                data = file.read()
                self.data = dict(eval(data))
                if self.data['language']:
                    self.language = self.data['language']
                else:
                    self.language = 'eng'
        except FileNotFoundError:
            with open('data.json', 'w') as file:
                self.language = 'eng'
                data = {'language': 'eng', 'high score': 0}
                json.dump(data, file)
        self.dictionary = languages.eng if self.language == 'eng' else languages.est
        self.screen_width = 1600
        self.screen_height = 1000
        self.bg_color = (17, 0, 29)
        # self.font_path = f'fonts/{self.language}_font.ttf'
        self.font_path = f'fonts/eng_font.ttf'
        self.flag_size = (70, 50)

        self.speed_up = 1.3

        # ship settings
        self.ship_speed = 3
        self.ship_size = [70, 100]
        self.change_frame_speed = 10
        self.ship_limit = 3
        self.ship_icon_size = [35, 50]

        # bullet settings
        self.bullet_speed = 4
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 0, 255, 0
        self.bullets_allowed = 3

        # alien settings
        self.alien_size = [82 * 1, 38 * 1]
        self.available_space = self.screen_width - 2 * self.alien_size[0]
        self.number_aliens_x = self.available_space / (2 * self.alien_size[0])
        self.available_space_y = self.screen_height - 6 * self.alien_size[1] - self.ship_size[1]
        self.available_rows = self.available_space_y / (3 * self.alien_size[1])
        self.alien_speed = 1.5
        self.fleet_drop_speed = 20
        # 1 represents right, -1 left
        self.fleet_direction = 1
        # score settings
        self.alien_points = 10
        self.point_increase = 1.5

        # turns
        self.fleets = 0

    def speed_up_game(self, stats):
        self.ship_speed *= self.speed_up
        self.bullet_speed *= (self.speed_up - 1) / 2 + 1
        self.alien_speed *= self.speed_up
        self.speed_up -= (self.speed_up - 1) / 10 if self.speed_up > 1.05 else 0

        # increase points to be gained and the current level
        self.alien_points *= self.point_increase
        stats.level += 1
