import json
from random import randint

import pygame

from bullet import Bullet
from alien import Alien
from background import Star, Planet
from time import sleep


def check_events(ai_settings, screen, ship, bullets, stats, play_button, eng_button, est_button):
    """check for any events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stats.quit = True

        # if a key is released
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

        # if a key is pressed
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets, stats)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, play_button, mouse_x, mouse_y)
            check_eng_button(stats, eng_button, mouse_x, mouse_y)
            check_est_button(stats, est_button, mouse_x, mouse_y)

        elif event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_over_play_button(play_button, mouse_x, mouse_y)
            check_over_eng_button(eng_button, mouse_x, mouse_y)
            check_over_est_button(est_button, mouse_x, mouse_y)


def draw_screen(ai_settings, screen, ship, bullets, aliens, stars, planets, game_over, stats, play_button, eng_button,
                est_button, scoreboard):
    """update images and draw new screen"""
    screen.fill(ai_settings.bg_color)
    for star in stars:
        star.blitme()
    for planet in planets:
        planet.blitme()
    if stats.game_started:
        if stats.game_over:
            game_over.blitme()
        else:
            for bullet in bullets:
                bullet.draw_bullet()
            aliens.draw(screen)
            ship.blitme()
        scoreboard.show_score()
    else:
        play_button.draw_button()
        eng_button.blitme()
        est_button.blitme()
        pygame.mouse.set_visible(True)

    # display the updated screen
    pygame.display.flip()


def check_keydown_events(event, ai_settings, screen, ship, bullets, stats):
    """check for key down events"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

    # command/uncomment to disable/enable vertical movement
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True

    elif event.key == pygame.K_SPACE and stats.game_started:
        fire_bullet(bullets, ai_settings, screen, ship)
    elif event.key == pygame.K_q:
        stats.quit = True
    elif event.key == pygame.K_r:
        stats.restart = True
    elif event.key == pygame.K_SPACE and not stats.game_started:
        stats.game_started = True
        stats.game_active = True
        pygame.mouse.set_visible(False)


def check_play_button(stats, play_button, mouse_x, mouse_y):
    """start a new game when the play button is clicked"""
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        stats.game_started = True
        stats.game_active = True
        pygame.mouse.set_visible(False)


def check_eng_button(stats, eng_button, mouse_x, mouse_y):
    """check whether English button is pressed"""
    if eng_button.rect.collidepoint(mouse_x, mouse_y):
        with open('data.json') as f:
            dict = json.load(f)
            if dict['language'] != 'eng':
                dict['language'] = 'eng'
                with open('data.json', 'w') as file:
                    json.dump(dict, file)
                stats.restart = True


def check_est_button(stats, est_button, mouse_x, mouse_y):
    """check whether English button is pressed"""
    if est_button.rect.collidepoint(mouse_x, mouse_y):
        with open('data.json') as f:
            dict = json.load(f)
            if dict['language'] != 'est':
                dict['language'] = 'est'
                with open('data.json', 'w') as file:
                    json.dump(dict, file)
                stats.restart = True


def check_over_play_button(play_button, mouse_x, mouse_y):
    """highlight the button when hovered over by the mouse"""
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        play_button.button_color = (155, 0, 0)
        play_button.button_color2 = (50, 50, 50)
    else:
        play_button.button_color = (128, 0, 255)
        play_button.button_color2 = (90, 0, 255)
    play_button.prep_msg(play_button.msg)


def check_over_eng_button(eng_button, mouse_x, mouse_y):
    """highlight the button"""
    if eng_button.rect.collidepoint(mouse_x, mouse_y):
        eng_button.color = (200, 200, 200)
    else:
        eng_button.color = (50, 50, 50)


def check_over_est_button(est_button, mouse_x, mouse_y):
    """highlight the button"""
    if est_button.rect.collidepoint(mouse_x, mouse_y):
        est_button.color = (200, 200, 200)
    else:
        est_button.color = (50, 50, 50)


def check_keyup_events(event, ship):
    """check for key up events"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def update_bullets(bullets, aliens, ai_settings, screen, scoreboard, stats, ship):
    """update the bullets"""

    # delete bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_collision(aliens, bullets, ai_settings, screen, scoreboard, stats, ship)

    # update the bullets
    bullets.update()


def fire_bullet(bullets, ai_settings, screen, ship):
    """fire a bullet"""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def create_fleet(ai_settings, screen, aliens, stats):
    """generate the alien fleet"""
    for row_number in range(int(ai_settings.available_rows)):
        for alien_number in range(int(ai_settings.number_aliens_x)):
            create_alien(ai_settings, screen, aliens, alien_number, row_number, stats)


def create_alien(ai_settings, screen, aliens, alien_number, row_number, stats):
    alien = Alien(ai_settings, screen, stats)
    alien.x = ai_settings.alien_size[0] + 2 * alien_number * ai_settings.alien_size[0]
    alien.rect.x = alien.x
    alien.y = ai_settings.alien_size[1] + 3 * row_number * ai_settings.alien_size[1]
    alien.rect.y = alien.y
    aliens.add(alien)


def update_aliens(aliens, ai_settings, ship, screen, stats, bullets):
    """updates the aliens"""
    check_fleet_edges(aliens, ai_settings)
    aliens.update(ship, aliens)
    # look for alien-ship collisions
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)


def check_fleet_edges(aliens, ai_settings):
    """respond, if any aliens have reached the edge"""
    for alien in aliens.sprites():
        if alien.check_edge():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """drop the entire fleet and change direction"""
    ai_settings.fleet_direction *= -1
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed


def check_aliens_left(aliens):
    """check whether there are any more aliens left"""
    if len(aliens) != 0:
        return True
    else:
        return False


def create_stars(screen, stars):
    """creates stars for the background"""
    for i in range(0, 100):
        star = Star(screen)
        star.rect.centerx = randint(0, star.screen_rect.width)
        star.rect.centery = randint(0, star.screen_rect.height)
        stars.add(star)
        star.x = float(star.rect.centerx)


def update_stars(stars):
    stars.update()


def create_planets(screen, planets, image_numbers):
    """creates stars for the background"""
    for i in range(0, 4):
        planet = Planet(screen, image_numbers)
        planet.rect.centerx = randint(-2000, planet.screen_rect.width)
        planet.rect.centery = randint(0, planet.screen_rect.height)
        planets.add(planet)
        planet.x = float(planet.rect.centerx)


def update_planets(planets, image_numbers):
    planets.update()


def check_bullet_collision(aliens, bullets, ai_settings, screen, scoreboard, stats, none):
    # check if any aliens are left
    if not check_aliens_left(aliens):
        bullets.empty()
        create_fleet(ai_settings, screen, aliens, stats)
        ai_settings.speed_up_game(stats)
        scoreboard.prep_score()

    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            # noinspection PyTypeChecker
            stats.score += ai_settings.alien_points * len(aliens)
            scoreboard.prep_score()


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """respond to ship being hit by aliens"""
    stats.ships_left -= 1
    aliens.empty()
    bullets.empty()
    if not stats.ships_left:
        stats.game_active = False
        stats.game_over = True

    create_fleet(ai_settings, screen, aliens, stats)
    ship.center_ship()
    sleep(1)


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """Check if any aliens have reached the bottom of the screen."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat this the same as if the ship got hit.
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break
