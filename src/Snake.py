import random
from enum import Enum
"""
Snake will be represented by an array of arrays:

[[x1,y1,d1],[x2,y2,d2],[x3,y3,d3],...]

xi - x coordinate of body element i

yi - y coordinate of body element i

di - direction of motion of body element i
    0 - left
    1 - up
    2 - right
    3 - down
"""


class Snake:

    def __init__(self, length, step, screen_width, screen_height):
        self.length = length
        self.step = step
        self.snake = []
        self.create_initial_snake(screen_width, screen_height)

    def create_initial_snake(self, screen_width, screen_height):
        d = random.randint(0, 3)
        x = random.randrange(0, screen_width - self.step*self.length, self.step)
        y = random.randrange(0, screen_height - self.step*self.length, self.step)

        for i in range(0, self.length):
            # Moving left - append to the right
            if d==0:
                self.snake.append([x + self.step*i, y, d])
            # Moving up - append to the bottom
            elif d==1:
                self.snake.append([x, y + self.step*i, d])
            # Moving right - append to the left
            elif d==2:
                self.snake.append([x - self.step*i, y, d])
            # Moving down - append up
            else:
                self.snake.append([x, y - self.step*i, d])

    def turn(self, direction):
        if self.flip_direction(direction) == self.snake[0][2]:
            return
        self.snake[0][2] = direction

    def move(self):
        new_head = self.get_next_pos(self.snake[0])
        self.snake.insert(0, new_head)
        self.snake.pop()
        # for i in range(1, len(self.snake)):
        #     self.snake[i] = self.get_next_pos(self.snake[i])
        #     self.snake[i][2] = self.snake[i-1][2]

    def grow(self):
        tail = self.snake[self.snake.length-1]
        tail[2] = self.flip_direction(tail[2])
        new_tail = self.get_next_pos(tail)
        new_tail[2] = self.snake[self.snake.length-1][2]
        self.snake.append(new_tail)

    def flip_direction(self, direction):
        if direction == 0:
            return 2
        elif direction == 1:
            return 3
        elif direction == 2:
            return 0
        else:
            return 1

    def get_next_pos(self, elem):
        x = elem[0]
        y = elem[1]
        d = elem[2]
        if d == 0:
            return [x - self.step, y, d]
        elif d == 1:
            return [x, y - self.step, d]
        elif d == 2:
            return [x + self.step, y, d]
        else:
            return [x, y + self.step, d]

    def get_snake(self):
        return self.snake

    def __repr__(self):
        return str(self.snake)


class Direction(Enum):
    Left = 0
    Up = 1
    Right = 2
    Down = 3

