import pygame
from pygame.sprite import Sprite


class Enemy_6(Sprite):
    def __init__(self,screen):
        super().__init__()
        self.screen=screen

        self.image = pygame.image.load("images/enemy_6.png")
        #self.image = pygame.image.load("images/pirate2.png")
        self.image=pygame.transform.scale(self.image,(250,300))
        self.rect=self.image.get_rect()
        self.screen_rect=self.screen.get_rect()


        self.rect.x=self.screen_rect.x+13500
        self.rect.y = self.screen_rect.y + 150

        self.moving_left=True

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.rect.centerx-=0.25