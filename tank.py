import pygame
from pygame.sprite import Sprite

class Tank(Sprite):

    def __init__(self, screen):  # инициализация гг танка
        
        super(Tank, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('space_game\\images\\tank.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.move_right = False
        self.move_left = False

    def output(self):  # отображение танка
        
        self.screen.blit(self.image, self.rect)

    def update_tank(self):  # обновление позиции танка

        if self.move_right and self.rect.right < self.screen_rect.right:
            self.center += 1.25
        if self.move_left and self.rect.left > self.screen_rect.left:  # или self.rect.left > 0
            self.center -= 1.25

        self.rect.centerx = self.center

    def create_tank(self):  # размещает tank по центру внизу

        self.center = self.screen_rect.centerx