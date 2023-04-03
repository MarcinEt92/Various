from Game import Game
from Player import Player
from Grid import Grid


player_1 = Player("Puś", "o")
player_2 = Player("Pusia", "x")

player = player_2


def change_player(current_player):
    if current_player == player_1:
        print(player_2)
        return player_2
    else:
        print(player_1)
        return player_1


while True:
    Grid.print_grid()
    player = change_player(player)
    number = Game.read_valid_number_from_user()
    Grid.update_grid(number, player)
    if Grid.is_a_winner():
        Game.clear_screen()
        Grid.print_grid()
        print(f"\n======== We have a winner: {player.name} ========")
        break
    if Grid.is_none_a_winner():
        print(f"\n======== We have no winners in this game ========")
        break
    Game.clear_screen()

print("\nEnd of The Game, Thank You!")
