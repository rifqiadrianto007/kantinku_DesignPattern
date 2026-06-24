from abc import ABC, abstractmethod

class MenuItem(ABC) :
    def __init__(self, name, price) :
        self.name = name
        self.price = price

    @abstractmethod
    def get_category(self) :
        pass

    def get_name(self) :
        return self.name

    def get_price(self) :
        return self.price

    def __str__(self) :
        return f"[{self.get_category()}] {self.get_name()} -> Rp{self.get_price():,}"

class FoodItem(MenuItem) :
    def get_category(self) :
        return "Food"

class DrinkItem(MenuItem) :
    def get_category(self) :
        return "Drink"

class MenuFactory :
    @staticmethod
    def create(category, name, price) :
        if category.lower() == "food" :
            return FoodItem(name, price)
        elif category.lower() == "drink" :
            return DrinkItem(name, price)
        raise ValueError("Invalid category")
