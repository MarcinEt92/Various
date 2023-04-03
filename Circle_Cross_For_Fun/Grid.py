

class Grid:
    values_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    marked_fields = []

    @classmethod
    def is_a_winner(cls):
        condition_1 = cls.values_list[0] == cls.values_list[1] == cls.values_list[2]
        condition_2 = cls.values_list[3] == cls.values_list[4] == cls.values_list[5]
        condition_3 = cls.values_list[6] == cls.values_list[7] == cls.values_list[8]
        condition_4 = cls.values_list[0] == cls.values_list[3] == cls.values_list[6]
        condition_5 = cls.values_list[1] == cls.values_list[4] == cls.values_list[7]
        condition_6 = cls.values_list[2] == cls.values_list[5] == cls.values_list[8]
        condition_7 = cls.values_list[0] == cls.values_list[4] == cls.values_list[8]
        condition_8 = cls.values_list[2] == cls.values_list[4] == cls.values_list[6]

        return any(
            [condition_1, condition_2, condition_3, condition_4, condition_5, condition_6, condition_7, condition_8])

    @classmethod
    def is_none_a_winner(cls):
        if (not cls.is_a_winner()) and len(cls.marked_fields) == len(cls.values_list):
            return True
        else:
            return False

    @classmethod
    def print_grid(cls):
        grid_string = f" {cls.values_list[0]} | {cls.values_list[1]} | {cls.values_list[2]}\n" + \
                      f" {cls.values_list[3]} | {cls.values_list[4]} | {cls.values_list[5]}\n" + \
                      f" {cls.values_list[6]} | {cls.values_list[7]} | {cls.values_list[8]}\n"
        print(grid_string)

    @classmethod
    def update_grid(cls, field_number, player):
        if field_number not in cls.marked_fields:
            cls.values_list[field_number - 1] = player.get_sign()
            cls.marked_fields.append(field_number)
