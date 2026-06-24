from factory import MenuItem

class MenuTopping(MenuItem) :
    def __init__(self, item, topping_name, topping_price) :
        self.item = item
        self.topping_name = topping_name
        self.topping_price = topping_price

    def get_category(self) :
        return self.item.get_category()

    def get_name(self) :
        return self.item.get_name() + " + " + self.topping_name

    def get_price(self) :
        return self.item.get_price() + self.topping_price
