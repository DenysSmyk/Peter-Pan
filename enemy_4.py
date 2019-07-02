import pygame
from pygame.sprite import Sprite


class Enemy_4(Sprite):
    def __init__(self,screen):
        super().__init__()
        self.screen=screen

        self.image = pygame.image.load("images/enemy_4.png")
        #self.image = pygame.image.load("images/pirate2.png")
        self.image=pygame.transform.scale(self.image,(170,200))
        self.rect=self.image.get_rect()
        self.screen_rect=self.screen.get_rect()


        self.rect.x=self.screen_rect.x+9500
        # self.rect.bottom=self.screen_rect.bottom
        self.rect.y = self.screen_rect.y + 50

        self.moving_left=True

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.rect.centerx-=0.25
