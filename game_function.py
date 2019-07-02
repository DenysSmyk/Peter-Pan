import pygame, sys
from bullet import Bullet
from pygame.sprite import Group
from random import randint
from enemy import Enemy
from friend import Friend
from time import sleep
from enemy_2 import Enemy_2
from hook import Hook


def chek_events(game_settings, ship, screen, bullets, button, stats, enemies, sb):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                ship.image = pygame.transform.scale(pygame.image.load("images/peter_pen_right.png"), (200, 250))

                ship.moving_right=True
            if event.key==pygame.K_LEFT:
                ship.moving_left = True
                ship.image = pygame.transform.scale(pygame.image.load("images/peter_pen_left.png"), (200, 250))

            if event.key==pygame.K_UP:
                ship.moving_up=True
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            if event.key==pygame.K_DOWN:
                ship.moving_down=True
            if event.key==pygame.K_SPACE:
                if len(bullets) < 50:
                    new_bullets=Bullet(game_settings,ship,screen)
                    bullets.add(new_bullets)
        if event.type == pygame.KEYUP:
            ship.image = pygame.transform.scale(pygame.image.load("images/peter_pan_stand.png"), (150, 200))



            if event.key == pygame.K_RIGHT:
                ship.moving_right = False

            if event.key == pygame.K_LEFT:
                ship.moving_left = False
                # ship.image="images/peter_pen_left.png"
            if event.key==pygame.K_UP:
                ship.moving_up=False
            if event.key==pygame.K_DOWN:
                ship.moving_down=False

        elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                check_play_button(button, mouse_x, mouse_y, stats, bullets, ship, game_settings, screen, enemies, sb)

def check_play_button(button, mouse_x, mouse_y, stats, bullets, ship, game_settings, screen, enemies, sb):
    if button.rect.collidepoint(mouse_x, mouse_y):
        stats.game_active = True
        stats.score = 0
        sb.prep_score()
        if stats.game_over == True:
            create_enemies(screen, enemies)
        stats.game_over = False

        #aliens.empty()
        bullets.empty()
        #create_fleet(game_settings, screen, ship)
        #ship.center_ship()
        stats.reset_stats()
        # game_settings.reset_speed()
        stats.score = 0

def create_enemies(screen, enemies):
    enemy = Enemy(screen)
    enemy_2 = Enemy_2(screen)
    hook = Hook(screen)
    enemies.add(enemy, enemy_2, hook)


def update_screen(background,ships,bullets,enemies,screen, button, friends,stats,sb):
    pygame.display.flip()
    #screen.fill(game_settings.bg_color)
    background.update()

    if stats.game_active == False:
        button.draw_button()
        if stats.game_over:
            # screen.blit.transform.scale(pygame.image.load("images/game_over.jpeg"), (0, 0)), (screen.image, (150, 200))
            screen.blit(pygame.image.load("images/game_over.jpeg"), (0, 0))
    sb.show_score()

def aliens_move(enemies, screen, friends, ships, bullets, ship):
    enemies.draw(screen)
    for enemy in enemies.copy():
        enemy.rect.x -=1
    for friend in friends.copy():
        friend.rect.x +=1
    #
    # ship.blitme()
    #ships.draw(screen)


    friends.draw(screen)

    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # if stats.game_active == False:
    #     button.draw_button()
    # sb.show_score()




def update_bullets(bullets, enemies, ships, friends, hook, stats, sb, screen):
    bullets.update()
    # print(len(enemies))
    # if
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullets)

    # collision = pygame.sprite.groupcollide(bullets, enemies, True, True)
    # if collision:
    #     stats.score += 1
    #     sb.prep_score()
    if stats.enemies_life > 0 and pygame.sprite.groupcollide(enemies, bullets, False, True):
        stats.enemies_life -= 1
        sb.prep_score()
        # print(stats.score, stats.enemies_life)
    elif stats.enemies_life == 0 and pygame.sprite.groupcollide(enemies, bullets, False, False):
        for bullet in bullets.copy():
            if pygame.sprite.collide_rect(bullet, hook):
                stats.game_active = False
                stats.game_over = True
        pygame.sprite.groupcollide(enemies, bullets, True, True)
        stats.score += 1
        stats.enemies_life = stats.score
        sb.prep_score()

    if pygame.sprite.groupcollide(enemies, ships, True, True):
        stats.game_active = False
        stats.game_over = True
    #if len(enemies) == 0



    if pygame.sprite.groupcollide(enemies, friends, True, True):
        stats.score += 1
        stats.enemies_life = stats.score
        sb.prep_score()


        # .screen.blit(self.score_image, self.score_rect)
        #       pygame.image.load("images/Tinkerbell.png")
        #      pygame.transform.scale(self.bullet_img, (70, 70))
