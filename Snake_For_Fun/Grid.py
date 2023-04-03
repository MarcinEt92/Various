import os


class Grid:
    x = 20
    y = 20
    grid_table = list()

    @staticmethod
    def clear_screen():
        os.system('clear')

    @classmethod
    def get_x(cls):
        return cls.x

    @classmethod
    def get_y(cls):
        return cls.y

    @classmethod
    def initialize(cls):
        cls.grid_table = [['  ' for _ in range(cls.get_x())] for _ in range(cls.get_y())]
        for i in range(0, cls.get_x()):
            for j in range(0, cls.get_y()):
                if i == 0 or j == 0 or i == cls.get_x() - 1 or j == cls.get_y() - 1:
                    cls.grid_table[i][j] = '* '

    @classmethod
    def print_grid(cls):
        for i in range(0, cls.get_x()):
            print('')
            for j in range(0, cls.get_y()):
                print(cls.grid_table[i][j], end='')
        print('')
