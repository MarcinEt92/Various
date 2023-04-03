from Game import Game
from Grid import Grid
from Point import Point

import random
import time


class Snake:
    all_snake_points = []
    food_point = Point(0, 0)
    game_speed = 0.4
    score = 0

    @classmethod
    def check_food_eaten_and_update_score(cls):
        snake_head = cls.all_snake_points[0]
        food_point = cls.food_point
        if snake_head == food_point:
            cls.food_point = cls.make_random_food()
            cls.all_snake_points.append(cls.create_new_snake_point())
            cls.score += 1

    @classmethod
    def create_new_snake_point(cls):
        new_point = Point(cls.all_snake_points[0].get_x(), cls.all_snake_points[0].get_y())
        if Game.direction == 'UP':
            new_point = Point(cls.all_snake_points[0].get_x() - 1, cls.all_snake_points[0].get_y())
        if Game.direction == 'DOWN':
            new_point = Point(cls.all_snake_points[0].get_x() + 1, cls.all_snake_points[0].get_y())
        if Game.direction == 'RIGHT':
            new_point = Point(cls.all_snake_points[0].get_x(), cls.all_snake_points[0].get_y() + 1)
        if Game.direction == 'LEFT':
            new_point = Point(cls.all_snake_points[0].get_x(), cls.all_snake_points[0].get_y() - 1)
        return new_point

    @classmethod
    def initialize(cls):
        cls.x = Grid.get_x() // 2
        cls.y = Grid.get_y() // 2
        cls.all_snake_points.append(Point(cls.x, cls.y))
        cls.food_point = cls.make_random_food()

    @classmethod
    def is_game_over(cls):
        snake_head = cls.all_snake_points[0]
        over_1 = snake_head.get_x() in (0, len(Grid.grid_table) - 1)
        over_2 = snake_head.get_y() in (0, len(Grid.grid_table) - 1)
        over_3 = snake_head in cls.all_snake_points[1:]
        return any((over_1, over_2, over_3))

    @classmethod
    def make_random_food(cls):
        snake_head = cls.all_snake_points[0]
        while True:
            rand_x = random.randrange(2, Grid.get_x() - 2)
            rand_y = random.randrange(2, Grid.get_y() - 2)
            food_point = Point(rand_x, rand_y)
            if snake_head != food_point:
                return food_point

    @classmethod
    def reset_point(cls, point):
        Grid.grid_table[point.get_x()][point.get_y()] = '  '

    @classmethod
    def set_point(cls, point):
        Grid.grid_table[point.get_x()][point.get_y()] = '* '

    @classmethod
    def update_snake_point_and_grid(cls):
        time.sleep(cls.game_speed)
        new_point = cls.create_new_snake_point()
        last_point = cls.all_snake_points.pop()

        cls.all_snake_points.insert(0, new_point)
        cls.reset_point(last_point)
        cls.set_point(cls.food_point)

        for snake_point in cls.all_snake_points:
            cls.set_point(snake_point)
