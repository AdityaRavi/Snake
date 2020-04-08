import random

class Food:

    def __init__(self, screen_width, screen_height, size):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.size = size
        self.move_food()

    def move_food(self):
        self.x = random.randrange(0, self.screen_width - self.size, self.size)
        self.y = random.randrange(0, self.screen_height - self.size, self.size)
        self.food = [self.x, self.y]

    def get_food(self):
        return self.food