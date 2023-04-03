from item import Item
from phone import Phone


Item.instantiate_from_csv()
item1 = Item("Calc", 80, 2)
item1.name = 'Calculator'
phone1 = Phone("Samsung", 120, 5)
print(Item.all)
