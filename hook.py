import pygame
from pygame.sprite import Sprite


class Hook(Sprite):
    def __init__(self,screen):
        super().__init__()

        self.screen=screen

        self.image=pygame.image.load("images/hook.gif")
        self.image=pygame.transform.scale(self.image, (450, 600))
        self.rect=self.image.get_rect()
        self.screen_rect=self.screen.get_rect()

        self.rect.x = self.screen_rect.x + 22000
        self.rect.centery = self.screen_rect.centery

        self.moving_left=True

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.rect.centerx -= 0.25