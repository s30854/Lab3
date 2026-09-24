from constants import TABLES, MENU_ITEMS


class Restaurant:

    def __init__(self):
        self.tables = [Table(seats, loc) for seats, loc in TABLES]
        self.menu_items = [MenuItem(name, price) for name, price in MENU_ITEMS]
        self.order=Order()
class Table:

    def __init__(self, seats, location):
        self.n_seats = seats
        self.location = location
        self.orders = [Order() for _ in range(seats)]

    def order_for(self, seat):
        return self.orders[seat-1]

class Order:
    def __init__(self):
        self.items=[]
        price=0


    def total_cost(self):
        for price in self.items:
            price += MENU_ITEMS[price.menu_item]

    def add_item(self,menu_item):
        self.items.append(menu_item)


class OrderItem:
    def __init__(self, menu_item):
        self.menu_item = menu_item


class MenuItem:

    def __init__(self, name, price):
        self.name = name
        self.price = price