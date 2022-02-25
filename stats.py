class Stats():  # отслеживание статистики

    def __init__(self):  # инициализация
        
        self.reset_stats()
        self.start_game = True
        with open('space_game\\highscore.txt', 'r') as file:
            self.highscore = int(file.readline())

    def reset_stats(self):  # статистика во время игры

        self.tank_drop = 2
        self.score = 0