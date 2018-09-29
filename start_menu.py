import pygame.font


# noinspection PyAttributeOutsideInit
class StartMenu:

    def __init__(self, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.menu_color = (0, 0, 0)
        self.text_color = (250, 250, 210)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.menu_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.screen_rect.center

    def draw_menu(self):
        self.screen.blit(self.msg_image, self.msg_image_rect)
