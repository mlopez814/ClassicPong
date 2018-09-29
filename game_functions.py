import sys
import pygame


def check_keydown_events(event, stats, sb, paddles, ball):
    if event.key == pygame.K_UP:
        paddles.moving_upR = True
    elif event.key == pygame.K_DOWN:
        paddles.moving_downR = True
    elif event.key == pygame.K_RIGHT:
        paddles.moving_right = True
    elif event.key == pygame.K_LEFT:
        paddles.moving_left = True
    elif event.key == pygame.K_SPACE:
        stats.game_active = True
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_r:
        ball.reset()
        stats.reset_stats()
        sb.computer_score()
        sb.player_score()


def check_keyup_events(event, paddles):
    if event.key == pygame.K_UP:
        paddles.moving_upR = False
    elif event.key == pygame.K_DOWN:
        paddles.moving_downR = False
    elif event.key == pygame.K_RIGHT:
        paddles.moving_right = False
    elif event.key == pygame.K_LEFT:
        paddles.moving_left = False


def check_events(stats, sb, paddles, ball):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, stats, sb, paddles, ball)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, paddles)


def check_ball_edges(screen, stats, sb, ball):
    screen_rect = screen.get_rect()
    if ball.check_edges():
        if ball.rect.centerx > screen_rect.centerx:
            stats.comp_score += 1
            sb.computer_score()
        else:
            stats.player_score += 1
            sb.player_score()
        ball.reset()
        stats.game_active = False


def check_ball_paddleH(ai_settings, ball):
    if ball.paddle_hitH():
        change_ball_directionV(ai_settings)


def check_ball_paddleV(ai_settings, ball):
    if ball.paddle_hitV():
        change_ball_directionH(ai_settings)


def change_ball_directionH(ai_settings):
    ai_settings.ball_directionH *= -1


def change_ball_directionV(ai_settings):
    ai_settings.ball_directionV *= -1


def check_collision(ai_settings, paddles, cp, ball):
    collidesL = pygame.Rect.colliderect(cp.c_paddleL, ball)
    collidesR = pygame.Rect.colliderect(paddles.paddleR, ball)

    c_collidesT = pygame.Rect.colliderect(cp.c_paddleT, ball)
    c_collidesB = pygame.Rect.colliderect(cp.c_paddleB, ball)

    collidesT = pygame.Rect.colliderect(paddles.paddleT, ball)
    collidesB = pygame.Rect.colliderect(paddles.paddleB, ball)

    if collidesL or collidesR:
        check_ball_paddleV(ai_settings, ball)
    if collidesT or collidesB:
        check_ball_paddleH(ai_settings, ball)
    if c_collidesT or c_collidesB:
        check_ball_paddleH(ai_settings, ball)


def update_ball(ai_settings, screen, stats, sb, paddles, cp, ball):
    check_collision(ai_settings, paddles, cp, ball)
    check_ball_edges(screen, stats, sb, ball)
    ball.update()


# noinspection SpellCheckingInspection
def computer_update(ai_settings, screen, cp, ball):
    centerT = float(cp.c_paddleT.centerx)
    centerL = float(cp.c_paddleL.centery)
    screen_rect = screen.get_rect()

    if ball.rect.left < screen_rect.centerx:
        if cp.c_paddleT.left > ball.rect.right:
            centerT -= ai_settings.paddle_speed
        if cp.c_paddleT.right < ball.rect.left:
            centerT += ai_settings.paddle_speed
    if ball.rect.left < screen_rect.centerx:
        if cp.c_paddleL.top > ball.rect.top:
            centerL -= ai_settings.paddle_speed
        if cp.c_paddleL.bottom < ball.rect.bottom:
            centerL += ai_settings.paddle_speed

    if ball.rect.left > screen_rect.centerx:
        if cp.c_paddleT.left > screen_rect.centerx/2:
            centerT -= ai_settings.paddle_speed
        if cp.c_paddleT.right < screen_rect.centerx/2:
            centerT += ai_settings.paddle_speed
    if ball.rect.left > screen_rect.centerx:
        if cp.c_paddleL.top > screen_rect.centery:
            centerL -= ai_settings.paddle_speed
        if cp.c_paddleL.bottom < screen_rect.centery:
            centerL += ai_settings.paddle_speed

    cp.c_paddleT.centerx = centerT
    cp.c_paddleB.centerx = centerT
    cp.c_paddleL.centery = centerL


def update_screen(ai_settings, screen, stats, sb, paddles, cp, ball, start_menu):
    screen.fill(ai_settings.bg_color)
    paddles.blitme()
    cp.blitme()
    ball.blitme()
    sb.show_score()

    if sb.check_winner:
        sb.show_winner()

    if not stats.game_active:
        start_menu.draw_menu()

    pygame.display.flip()
