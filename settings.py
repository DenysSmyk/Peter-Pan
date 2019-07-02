import pygame

class Settings():
    def __init__(self):
        self.screen_width=1300
        self.screen_height=600
        # self.bg_color=(100,82,120)

        self.bullet_width = 10
        self.bullet_height = 10
        self.bullet_color = 120, 120, 120
        self.bullet_speed_factor = 3

        self.clock = pygame.time.Clock()


