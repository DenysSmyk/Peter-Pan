import pygame
from pygame.sprite import Sprite


class Enemy_9(Sprite):
    def __init__(self,screen):
        super().__init__()
        self.screen=screen

        self.image = pygame.image.load("images/enemy_9.gif")
        #self.image = pygame.image.load("images/pirate2.png")
        self.image=pygame.transform.scale(self.image,(370,420))
        self.rect=self.image.get_rect()
        self.screen_rect=self.screen.get_rect()


        self.rect.x=self.screen_rect.x+19500
        self.rect.bottom=self.screen_rect.bottom

        self.moving_left=True

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.rect.centerx-=0.25