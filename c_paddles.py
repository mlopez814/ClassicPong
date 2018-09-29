import pygame
from pygame.sprite import Sprite


class CPaddles(Sprite):

    def __init__(self, ai_settings, screen):
        super(CPaddles, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.imageT = pygame.image.load('images/paddleH.png')
        self.imageR = pygame.image.load('images/paddleV.png')
        self.imageF = pygame.image.load('images/field.png')
        self.c_paddleT = self.imageT.get_rect()
        self.c_paddleB = self.imageT.get_rect()
        self.c_paddleL = self.imageR.get_rect()
        self.field = self.imageF.get_rect()
        self.screen_rect = screen.get_rect()

        self.c_paddleT.centerx = self.screen_rect.centerx/2
        self.c_paddleT.top = self.screen_rect.top + 10

        self.c_paddleB.centerx = self.screen_rect.centerx/2
        self.c_paddleB.bottom = self.screen_rect.bottom - 10

        self.c_paddleL.centery = self.screen_rect.centery
        self.c_paddleL.left = self.screen_rect.left + 10

        self.field.centerx = self.screen_rect.centerx

        self.centerT = float(self.c_paddleT.centerx)
        self.centerL = float(self.c_paddleL.centery)
        self.moving_upL = False
        self.moving_downL = False

    def blitme(self):
        self.screen.blit(self.imageT, self.c_paddleT)
        self.screen.blit(self.imageT, self.c_paddleB)
        self.screen.blit(self.imageR, self.c_paddleL)
        self.screen.blit(self.imageF, self.field)
