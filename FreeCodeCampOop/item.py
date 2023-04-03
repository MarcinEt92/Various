import csv


class Item:
    pay_rate = 0.8  # pay rate after 20% discount, global discount for all items
    all = []

    def __init__(self, name: str, price: float = 0, quantity: int = 0):
        # Arguments Validation:
        assert type(name) == str, f"{name} is not str type but {type(name)}"
        assert price >= 0, f"Actual price of {name} is {price}, should be >= 0"
        assert quantity >= 0, f"Actual quantity of {name} is {quantity}, should be >= 0"

        # Assignments:
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # Actions:
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.__price}, {self.quantity})"

    @property
    # property decorator - read only attribute
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 2:
            raise Exception("Name should have at least 2 characters")
        self.__name = value

    @property
    def price(self):
        return self.__price

    @classmethod
    def instantiate_from_csv(cls):
        with open('csv_files/items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    def calculate_total_price(self):
        return self.__price * self.quantity

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

    @staticmethod
    def is_integer(number):
        if isinstance(number, float):
            return number.is_integer()
        elif isinstance(number, int):
            return True
        else:
            return False
