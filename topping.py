from factory import MenuItem

class MenuTopping(MenuItem) :
    def __init__(self, item) :
        self.item = item

    def get_category(self) :
        return self.item.get_category()

    def get_name(self) :
        return self.item.get_name()

    def get_price(self) :
        return self.item.get_price()

class MilkTopping(MenuTopping) :
    def get_name(self) :
        return self.item.get_name() + " + Milk"

    def get_price(self):
        return self.item.get_price() + 3000


class SugarTopping(MenuTopping) :
    def get_name(self) :
        return self.item.get_name() + " + Sugar"
    def get_price(self):
        return self.item.get_price() + 1000

class CheeseTopping(MenuTopping) :
    def get_name(self) :
        return self.item.get_name() + " + Cheese"

    def get_price(self) :
        return self.item.get_price() + 5000