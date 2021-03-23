# the main file for the project in which things are executed and ran
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from game_over import GameOver
from button import Button
from languages import Languages, EngButton, EstButton
from scoreboard import Scoreboard
import time
restart = True


def run_game():
    """starts the game and draws screen"""
    pygame.init()
    languages = Languages()
    ai_settings = Settings(languages)
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # make the bullets and aliens group and a ship
    bullets = Group()
    aliens = Group()
    ship = Ship(screen, ai_settings)
    stats = GameStats(ai_settings)
    stars = Group()
    planets = Group()
    game_over = GameOver(screen, ai_settings)
    play_button = Button(ai_settings, screen)
    eng_button = EngButton(ai_settings, screen)
    est_button = EstButton(ai_settings, screen)
    clock = pygame.time.Clock()
    scoreboard = Scoreboard(ai_settings, stats, screen)

    image_numbers = ['0', '1', '2', '3', '4', '5', '6', '7']

    # create a fleet of aliens
    gf.create_fleet(ai_settings, screen, aliens, stats)
    stats.created = True
    gf.create_stars(screen, stars)
    gf.create_planets(screen, planets, image_numbers)
    # start the main loop
    while True:
        # check for any events such as quit
        gf.check_events(ai_settings, screen, ship, bullets, stats, play_button, eng_button, est_button)

        # update ship and bullets
        if stats.game_active:
            ship.update()
            gf.update_bullets(bullets, aliens, ai_settings, screen, scoreboard, stats, ship)
            gf.update_aliens(aliens, ai_settings, ship, screen, stats, bullets)
        if stats.restart or stats.quit:
            if stats.restart:
                global restart
                restart = True
            stats.save_high_score()
            break

        stars.update()
        planets.update(image_numbers)

        # update the screen
        gf.draw_screen(ai_settings, screen, ship, bullets, aliens, stars, planets, game_over, stats, play_button,
                       eng_button, est_button, scoreboard)

        clock.tick(120)


while restart:
    restart = False
    run_game()
