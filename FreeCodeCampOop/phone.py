from item import Item


class Phone(Item):

    def __init__(self, name: str, price: float = 0, quantity: int = 0, is_broken: bool = False):
        # Arguments Validation:
        assert isinstance(is_broken, bool), f"is_broken attribute is {type(is_broken)} while it shout be bool"

        # Assignments:
        super().__init__(name, price, quantity)
        self.is_broken = is_broken



