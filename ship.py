import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    def __init__(self,screen):
        super().__init__()
        self.screen=screen

        self.image=pygame.image.load("images/peter_pan_stand.png")

        self.image=pygame.transform.scale(self.image, (150, 200))
        self.rect=self.image.get_rect()
        self.screen_rect=self.screen.get_rect()

        self.rect.y=self.screen_rect.y+200
        self.rect.x=self.screen_rect.x+200

        self.moving_right=False
        self.moving_left=False
        self.moving_up=False
        self.moving_down=False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.rect.centerx +=3
        if self.moving_left and self.rect.left>0:
            self.rect.centerx -=3
        if self.moving_up and self.rect.top>0:
            self.rect.centery -=3
        if self.moving_down and self.rect.bottom<self.screen_rect.bottom:
            self.rect.centery +=3
