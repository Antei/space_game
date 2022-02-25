import pygame

class Bullet(pygame.sprite.Sprite):
    
    def __init__(self, screen, tank):  # создаем снаряд в текущей позиции танка
        
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 4, 12)
        self.color = 255, 40, 40
        self.speed = 4.5
        self.rect.centerx = tank.rect.centerx
        self.rect.top = tank.rect.top
        self.y = float(self.rect.y)

    def update(self):  # перемещение снаряда вверх
        
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):  # отрисовка пули
        
        pygame.draw.rect(self.screen, self.color, self.rect)