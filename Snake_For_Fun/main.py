from Grid import Grid
from KeyboardLogger import KeyboardLogger
from Snake import Snake


Grid.initialize()
Snake.initialize()
KeyboardLogger.start_logging()

while True:
    if Snake.is_game_over():
        break
    Snake.update_snake_point_and_grid()
    Snake.check_food_eaten_and_update_score()
    Grid.clear_screen()
    Grid.print_grid()

print(f"Game Over, Your Score: {Snake.score} points")

# https://docs.python.org/3/howto/curses.html
