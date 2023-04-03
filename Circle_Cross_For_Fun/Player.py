class Player:
    def __init__(self, name, sign):
        self.name = name
        self.sign = sign

    def __str__(self):
        return f"Player {self.name} with {self.sign} sign:"

    def get_sign(self):
        return self.sign
