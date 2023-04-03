from pynput.keyboard import Key, Listener

from Game import Game


class KeyboardLogger:
    @classmethod
    def on_press(cls, key):
        if key == Key.up and Game.direction != "DOWN":
            Game.direction = 'UP'
        if key == Key.down and Game.direction != "UP":
            Game.direction = 'DOWN'
        if key == Key.right and Game.direction != "LEFT":
            Game.direction = 'RIGHT'
        if key == Key.left and Game.direction != "RIGHT":
            Game.direction = 'LEFT'

    @classmethod
    def start_logging(cls):
        listener = Listener(on_press=cls.on_press)
        listener.start()
