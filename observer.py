class Observer :
    def update(self, order) :
        pass

class KitchenObserver(Observer) :
    def update(self, order) :
        if order.status == "Confirmed" :
            print(f"[KITCHEN] Cooking Order #{order.order_id}")

class CashierObserver(Observer) :
    def update(self, order) :
        if order.status == "Confirmed" :
            print(f"[CASHIER] Order #{order.order_id} total = Rp{order.total():,}")
        elif order.status == "Completed" :
            print(f"[CASHIER] Order #{order.order_id} complete")

class DisplayObserver(Observer) :
    def update(self, order) :
        print(f"[DISPLAY] Order #{order.order_id} - {order.status}")

class OrderSubject :
    next_id = 1
    def __init__(self, customer_name) :
        self.order_id = OrderSubject.next_id
        OrderSubject.next_id += 1
        self.customer_name = customer_name
        self.items = []
        self.status = "Processing"
        self.observers = []

    def attach(self, observer) :
        self.observers.append(observer)

    def notify(self) :
        for observer in self.observers :
            observer.update(self)

    def add_item(self, item, qty = 1) :
        self.items.append({"item": item, "qty": qty})

    def total(self) :
        total = 0
        for data in self.items :
            total += data["item"].get_price() * data["qty"]
        return total

    def confirm(self) :
        self.status = "Confirmed"
        self.notify()

    def complete(self) :
        self.status = "Completed"
        self.notify()

    def show_order(self) :
        print(f"Order #{self.order_id}")
        print(f"Customer : {self.customer_name}")

        for data in self.items :
            item = data["item"]
            qty = data["qty"]
            print(f"{qty} x {item.get_name()} -> Rp{item.get_price() * qty:,}")

        print("-" * 40)
        print(f"TOTAL : Rp{self.total():,}")
