import json


class GameStats:
    """a class for tracking score and lives etc"""
    def __init__(self, ai_settings):
        """initialize the game stats"""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        self.game_over = False
        self.restart = False
        self.game_started = False
        self.quit = False
        self.created = False
        self.ships_left = ai_settings.ship_limit

        self.score = 0
        self.level = 1

        with open('data.json', 'r') as f:
            data = json.load(f)
            self.high_score = data['high score']

    def reset_stats(self):
        """initialize stats that change mid game"""
        self.ships_left = self.ai_settings.ship_limit

    def save_high_score(self):
        with open('data.json') as f:
            data = json.load(f)
            if self.score > data['high score']:
                data['high score'] = self.score
                with open('data.json', 'w') as file:
                    json.dump(data, file)
