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
        return self.orders[seat]

    def has_order_for(self, seat):
        order = self.order_for(seat)
        return bool(order.items) and not order.unordered_items()

class Order:
    def __init__(self):
        self.items=[]

    def total_cost(self):
        return sum(item.details.price for item in self.items)

    def add_item(self,menu_item):
        self.items.append(OrderItem(menu_item))

    def unordered_items(self):
        return [item for item in self.items if not item.ordered]

    def place_new_orders(self):
        for item in self.unordered_items():
            item.mark_as_ordered()
    
    def remove_unordered_items(self):
        self.items = [item for item in self.items if item.ordered]

class OrderItem:
    def __init__(self, menu_item):
        self.details = menu_item
        self.ordered = False

    def mark_as_ordered(self):
        self.ordered = True

class MenuItem:

    def __init__(self, name, price):
        self.name = name
        self.price = price