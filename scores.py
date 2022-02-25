import pygame.font
from tank import Tank
from pygame.sprite import Group

class Scores():  # вывод игровой статистики

    def __init__(self, screen, stats):  # инициализация подсчета очков

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = 200, 200, 200
        self.font = pygame.font.SysFont('Calibri', 30)
        self.image_score()
        self.image_highscore()
        self.image_tanks()

    def image_score(self):  # преобразование текста score в изображение

        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (30, 30, 30))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 50
        self.score_rect.top = 20

    def image_highscore(self):  # преобразование текста highscore в изображение

        self.highscore_img = self.font.render(str(self.stats.highscore), True, self.text_color, (30, 30, 30))
        self.highscore_rect = self.highscore_img.get_rect()
        self.highscore_rect.centerx = self.screen_rect.centerx
        self.highscore_rect.top = self.screen_rect.top + 20

    def image_tanks(self):  # количество жизней

        self.tanks = Group()
        for live_counter in range(self.stats.tank_drop):
            tank = Tank(self.screen)
            tank.rect.x = 15 + live_counter * tank.rect.width
            tank.rect.y = 20
            self.tanks.add(tank)

    def show_score(self):  # вывод score на экран

        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.highscore_img, self.highscore_rect)
        self.tanks.draw(self.screen)