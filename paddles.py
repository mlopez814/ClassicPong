import pygame
from pygame.sprite import Sprite


class Paddles(Sprite):

    def __init__(self, ai_settings, screen):
        super(Paddles, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.imageT = pygame.image.load('images/paddleH.png')
        self.imageR = pygame.image.load('images/paddleV.png')
        self.paddleT = self.imageT.get_rect()
        self.paddleB = self.imageT.get_rect()
        self.paddleR = self.imageR.get_rect()
        self.screen_rect = screen.get_rect()

        self.paddleT.centerx = self.screen_rect.centerx + self.screen_rect.centerx/2
        self.paddleT.top = self.screen_rect.top + 10

        self.paddleB.centerx = self.screen_rect.centerx + self.screen_rect.centerx/2
        self.paddleB.bottom = self.screen_rect.bottom - 10

        self.paddleR.centery = self.screen_rect.centery
        self.paddleR.right = self.screen_rect.right - 10

        self.centerT = float(self.paddleT.centerx)
        self.centerR = float(self.paddleR.centery)

        self.moving_left = False
        self.moving_right = False

        self.moving_upR = False
        self.moving_downR = False

    def update(self):
        if self.moving_left and self.paddleT.left > self.screen_rect.centerx:
            self.centerT -= self.ai_settings.paddle_speed
        if self.moving_right and self.paddleT.right < self.screen_rect.right:
            self.centerT += self.ai_settings.paddle_speed

        if self.moving_upR and self.paddleR.top > 0:
            self.centerR -= self.ai_settings.paddle_speed
        if self.moving_downR and self.paddleR.bottom < self.screen_rect.bottom:
            self.centerR += self.ai_settings.paddle_speed

        self.paddleT.centerx = self.centerT
        self.paddleB.centerx = self.centerT
        self.paddleR.centery = self.centerR

    def blitme(self):
        self.screen.blit(self.imageT, self.paddleT)
        self.screen.blit(self.imageT, self.paddleB)
        self.screen.blit(self.imageR, self.paddleR)
