import pygame, controls
from tank import Tank
from pygame.sprite import Group
from stats import Stats
from scores import Scores

def start():

    pygame.init()
    screen = pygame.display.set_mode((720, 720), 1, 1, 0, 1)
    pygame.display.set_caption('space game')
    bg_color = (30, 30, 30)
    tank = Tank(screen)
    bullets = Group()
    enemyes = Group()
    controls.create_squad(screen, enemyes)
    stats = Stats()
    score = Scores(screen, stats)

    while True:

        controls.events(screen, tank, bullets)
        if stats.start_game:
            tank.update_tank()
            controls.update_screen(bg_color, screen, stats, score, tank, bullets, enemyes)
            controls.update_bullets(screen, stats, score, bullets, enemyes)
            controls.update_enemyes(stats, screen, score, tank, enemyes, bullets)

start()