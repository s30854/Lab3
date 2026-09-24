from model import Table


class Controller:
    """
    Do not modify this class, just its subclasses. Represents common behaviour of all
    Controllers. Python has a mechanism for explicitly dealing with abstract classes,
    which we haven't seen yet; raising RuntimeError gives a similar effect.
    """

    def __init__(self, view, restaurant):
        self.view = view
        self.restaurant = restaurant
        self.table = None
        self.seat_number=None

    def add_item(self, item):
        raise RuntimeError('add_item: some subclasses must implement')

    def cancel(self):
        raise RuntimeError('cancel: some subclasses must implement')

    def create_ui(self):
        raise RuntimeError('create_ui: all subclasses must implement')

    def done(self):
        self.view.set_controller(RestaurantController(self.view, self.restaurant))

    def place_order(self):
        raise RuntimeError('place_order: some subclasses must implement')

    def seat_touched(self, seat_number):
        self.seat_number = self.table.n_seats
        self.view.set_controller(OrderController(self.view, self.restaurant,self.table, self.seat_number))

    def table_touched(self, table_number):
        self.table = self.restaurant.tables[table_number]
        self.view.set_controller(TableController(self.view, self.restaurant,self.table))


class RestaurantController(Controller):

    def create_ui(self):
        self.view.create_restaurant_ui()


class TableController(Controller):

    def __init__(self, view, restaurant, table):
        super().__init__(view, restaurant)
        self.view = view
        self.restaurant = restaurant
        self.table = table

    def create_ui(self):
        self.view.create_table_ui(self.table)



class OrderController(Controller):
    def __init__(self,view, restaurant,table, seat_number):
        super().__init__(view, restaurant)
        self.seat_number = seat_number
        self.restaurant = restaurant
        self.table = table
        self.seat_number = seat_number
    def create_ui(self):
        self.view.create_order_ui(self.table.order_for(self.seat_number))

    def add_item(self, menu_item):
        self.restaurant.add_item(menu_item)