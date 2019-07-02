import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,game_settings,ship,screen):
        super().__init__()

        self.screen=screen

        self.bullet_img=pygame.image.load("images/Tinkerbell.png")
        self.bullet_img=pygame.transform.scale(self.bullet_img,(70,70))

        self.rect=self.bullet_img.get_rect()
        self.screen_rect=self.screen.get_rect()

        self.rect.x=ship.rect.x+100
        self.rect.top=ship.rect.top
        self.rect.y = ship.rect.y+50

        self.speed_factor=game_settings.bullet_speed_factor

    def update(self):
        self.rect.x += self.speed_factor

        if self.rect.right > self.screen_rect.right:
            self.kill()

    def draw_bullet(self):
        self.screen.blit(self.bullet_img, self.rect)