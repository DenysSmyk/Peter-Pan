import pygame,sys
from settings import Settings
from ship import Ship
from friend import Friend
from enemy import Enemy
from enemy_2 import Enemy_2
from enemy_3 import Enemy_3
from enemy_4 import Enemy_4
from enemy_5 import Enemy_5
from enemy_6 import Enemy_6
from enemy_7 import Enemy_7
from enemy_8 import Enemy_8
from enemy_9 import Enemy_9
from hook import Hook
import game_function as g_f
from pygame.sprite import Group
from background import Background
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def init_game():
    pygame.init()

    game_settings = Settings()

    screen=pygame.display.set_mode((game_settings.screen_width,game_settings.screen_height), pygame.FULLSCREEN)
    # screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    ship=Ship(screen)
    stats=GameStats(game_settings)
    friend=Friend(screen)

    enemy = Enemy(screen)
    enemy_2 = Enemy_2(screen)
    enemy_3 = Enemy_3(screen)
    enemy_4 = Enemy_4(screen)
    enemy_5 = Enemy_5(screen)
    enemy_6 = Enemy_6(screen)
    enemy_7 = Enemy_7(screen)
    enemy_8 = Enemy_8(screen)
    enemy_9 = Enemy_9(screen)

    hook=Hook(screen)
    background=Background(screen)
    pygame.display.set_caption("Peter Pan")

    bullets=Group()
    enemies = Group()
    enemies.add(enemy, enemy_2, enemy_3, enemy_4, enemy_5, enemy_6, enemy_7, enemy_8, enemy_9, hook)
    friends=Group()
    friends.add(friend)
    ships=Group()
    ships.add(ship)
    #g_f.create_fleet(game_settings, screen, ship)
    button = Button(screen, game_settings, "Play")
    sb = Scoreboard(game_settings, screen, stats)



    while True:
        g_f.chek_events(game_settings, ship, screen, bullets, button, stats, enemies, sb)
        g_f.update_screen(background, ships, bullets, enemies, screen, button, friends, stats, sb)

        if stats.game_active:
            g_f.update_bullets(bullets, enemies, ships, friends, hook, stats, sb, screen)
            g_f.aliens_move(enemies, screen, friends, ships, bullets, ship)

            ship.update()
            ship.blitme()


init_game()
