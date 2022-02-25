import pygame, sys
from bullet import Bullet
from enemy import Enemy
import time

def events(screen, tank, bullets):  # обработка событий управления
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:  # движение вправо
                tank.move_right = True
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:  # движение влево
                tank.move_left = True
            if event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, tank)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                tank.move_right = False
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                tank.move_left = False

def update_screen(bg_color, screen, stats, score, tank, bullets, enemyes):  # обновление экрана
    
    screen.fill(bg_color)
    score.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    tank.output()
    enemyes.draw(screen)
    pygame.display.flip()

def update_bullets(screen, stats, score, bullets, enemyes): # обновление позиции снарядов
    
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, enemyes, True, True)
    if collisions:
        for enemyes in collisions.values():
            stats.score += 1 * len(enemyes)
        score.image_score()
        highscore_check(stats, score)
        score.image_tanks()
    if len(enemyes) == 0:
        bullets.empty()
        create_squad(screen, enemyes)        

def tank_kill(stats, screen, score, tank, enemyes, bullets):  # столкновение tank и enemyes

    if stats.tank_drop > 0:
        stats.tank_drop -= 1
        score.image_tanks()
        enemyes.empty()
        bullets.empty()
        create_squad(screen, enemyes)
        tank.create_tank()
        time.sleep(1)
    else:
        stats.start_game = False
        sys.exit()

def update_enemyes(stats, screen, score, tank, enemyes, bullets):  # обновляет позицию enemyes

    enemyes.update()
    if pygame.sprite.spritecollideany(tank, enemyes):
        tank_kill(stats, screen, score, tank, enemyes, bullets)
    check_border(stats, screen, score, tank, enemyes, bullets)

def check_border(stats, screen, score, tank, enemyes, bullets):  # проверка, не добрались ли enemyes до границы

    screen_rect = screen.get_rect()
    for en in enemyes.sprites():
        if en.rect.bottom >= screen_rect.bottom:
            tank_kill(stats, screen, score, tank, enemyes, bullets)
            break


def create_squad(screen, enemyes):  # создание отряда enemyes

    enemy = Enemy(screen)
    enemy_width = enemy.rect.width
    enemy_height = enemy.rect.height + 22
    size_squad_x = int((720 - 2 * 50) / 50)
    size_squad_y = int((720 - 200 - 2 * 50) / enemy_height)

    for row in range(size_squad_y - 2):
        for col in range(size_squad_x):
            enemy = Enemy(screen)
            enemy.x = 60 + enemy_width * col
            enemy.y = 100 + enemy_height * row
            enemy.rect.x = enemy.x
            enemy.rect.y = enemy.y
            enemyes.add(enemy)

def highscore_check(stats, score):  # проверка новых рекордов

    if stats.score > stats.highscore:
        stats.highscore = stats.score
        score.image_highscore()
        with open('space_game\\highscore.txt', 'w') as file:
            file.write(str(stats.highscore))