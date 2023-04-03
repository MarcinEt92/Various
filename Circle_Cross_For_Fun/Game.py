import os
from Grid import Grid


class Game:

    @staticmethod
    def get_a_valid_number(value):
        try:
            num = int(value)
        except ValueError:
            print("probably not a number, try again")
            return None
        else:
            if num in range(1, 10) and num not in Grid.marked_fields:
                return num
            else:
                print("number not in range 1 - 9, or was marked before, try again")
                return None

    @staticmethod
    def read_valid_number_from_user():
        while True:
            value = input("Enter a Number from 1-9: ").strip()
            num_value = Game.get_a_valid_number(value)
            if isinstance(num_value, int):
                break
        return num_value

    @staticmethod
    def clear_screen():
        os.system('clear')
