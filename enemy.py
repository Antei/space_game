import pygame

class Enemy(pygame.sprite.Sprite):  # класс одного enemy

    def __init__(self, screen):  # инициализация и определение начальной позиции

        super(Enemy, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('space_game\images\enemy.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):  # вывод enemy на экран

        self.screen.blit(self.image, self.rect)

    def update(self):  # перемещает enemy

        self.y += 0.05
        self.rect.y = self.y