import pygame
from pygame.sprite import Sprite


class Friend(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen=screen

        self.image=pygame.image.load("images/friend.png")
        self.image=pygame.transform.scale(self.image,(140,180))
        self.rect=self.image.get_rect()
        self.screen_rect=self.screen.get_rect()


        self.rect.x=self.screen_rect.x-5600
        self.rect.y=self.screen_rect.y+100
        # self.rect.bottom = self.screen_rect.bottom


        self.moving_left=True

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.rect.centerx-=0.25