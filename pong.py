import pygame

from settings import Settings
from paddles import Paddles
from c_paddles import CPaddles
from ball import Ball
from game_stats import GameStats
from scoreboard import Scoreboard
from start_menu import StartMenu
import game_functions as gf


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    start_menu = StartMenu(screen, "'SPACE' to start, 'R' to reset")

    paddles = Paddles(ai_settings, screen)
    cp = CPaddles(ai_settings, screen)
    ball = Ball(ai_settings, screen, paddles, cp)

    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats, ball)

    while True:
        gf.check_events(stats, sb, paddles, ball)

        if stats.game_active:
            paddles.update()
            gf.computer_update(ai_settings, screen, cp, ball)
            gf.update_ball(ai_settings, screen, stats, sb, paddles, cp, ball)

        gf.update_screen(ai_settings, screen, stats, sb, paddles, cp, ball, start_menu)


run_game()
