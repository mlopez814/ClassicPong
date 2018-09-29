from random import randint

import pygame
from pygame.sprite import Sprite


# noinspection PyPep8Naming
class Ball(Sprite):

    def __init__(self, ai_settings, screen, paddles, cp):
        super(Ball, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.paddles = paddles

        self.cp = cp

        self.image = pygame.image.load("images/ball.png")
        self.rect = self.image.get_rect()

        self.rect.centery = 300
        self.rect.centerx = 600

        self.centerH = float(self.rect.centerx)
        self.centerV = float(self.rect.centery)

        self.speedH = randint(10, 15)
        self.speedV = randint(10, 15)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        elif self.rect.top <= 0:
            return True
        elif self.rect.bottom >= screen_rect.bottom:
            return True

    def paddle_hitH(self):
        paddleT = self.paddles.paddleT
        paddleB = self.paddles.paddleB

        c_paddleT = self.cp.c_paddleT
        c_paddleB = self.cp.c_paddleB

        if self.rect.top <= paddleT.bottom:
            return True
        elif self.rect.bottom >= paddleB.top:
            return True
        elif self.rect.top <= c_paddleT.bottom:
            return True
        elif self.rect.bottom >= c_paddleB.top:
            return True

    def paddle_hitV(self):
        paddleR = self.paddles.paddleR
        paddleL = self.cp.c_paddleL

        if self.rect.right >= paddleR.left:
            return True
        elif self.rect.left < paddleL.right:
            return True

    def update(self):
        self.centerH += (self.speedH * self.ai_settings.ball_directionH)
        self.centerV += (self.speedV * self.ai_settings.ball_directionV)

        self.rect.centerx = self.centerH
        self.rect.centery = self.centerV

    #create ball after spawn with different H/V velocities
    def reset(self):
        self.centerH = 600
        self.centerV = 300
        self.rect.centerx = self.centerH
        self.rect.centery = self.centerV
        self.speedH = randint(10, 15)
        self.speedV = randint(10, 15)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
