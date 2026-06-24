from factory import MenuFactory
from observer import OrderSubject, KitchenObserver, CashierObserver, DisplayObserver
from topping import MenuTopping

MENU_DB = {
    1: {"category": "Drink", "name": "Americano", "price": 20000},
    2: {"category": "Drink", "name": "Latte", "price": 24000},
    3: {"category": "Drink", "name": "Tea", "price": 12000},
    4: {"category": "Food", "name": "Toast Bread", "price": 15000},
    5: {"category": "Food", "name": "French Fries", "price": 18000},
    6: {"category": "Food", "name": "Chicken Sandwich", "price": 28000},
}

TOPPING_DB = {
    1: {
        "name": "Milk",
        "price": 3000,
        "categories": ["Drink"],
    },
    2: {
        "name": "Sugar",
        "price": 1000,
        "categories": ["Drink"],
    },
    3: {
        "name": "Cheese",
        "price": 5000,
        "categories": ["Food"],
    },
}

ORDER_DB = {}

def format_rupiah(amount):
    return f"Rp{amount:,}"

def input_text(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input tidak boleh kosong.")

def input_number(prompt, valid_options=None, minimum=None):
    while True:
        value = input(prompt).strip()
        if not value.isdigit():
            print("Masukkan angka yang valid.")
            continue

        number = int(value)
        if valid_options is not None and number not in valid_options:
            print("Pilihan tidak tersedia.")
            continue

        if minimum is not None and number < minimum:
            print(f"Masukkan angka minimal {minimum}.")
            continue

        return number

def input_yes_no(prompt):
    while True:
        value = input(prompt).strip().lower()
        if value in ["y", "ya"]:
            return True
        if value in ["n", "tidak"]:
            return False
        print("Jawab dengan y/ya atau n/tidak.")

def show_menu():
    print("\n==== MENU KANTINKU ====")
    for item_id, data in MENU_DB.items():
        print(
            f"{item_id}. [{data['category']}] {data['name']} - "
            f"{format_rupiah(data['price'])}"
        )

def show_toppings(category):
    available_toppings = {
        topping_id: data
        for topping_id, data in TOPPING_DB.items()
        if category in data["categories"]
    }

    if not available_toppings:
        print("Tidak ada topping untuk menu ini.")
        return {}

    print("\nTopping tersedia:")
    print("0. Tanpa topping")
    for topping_id, data in available_toppings.items():
        print(f"{topping_id}. {data['name']} (+{format_rupiah(data['price'])})")

    return available_toppings

def build_menu_item(menu_data):
    return MenuFactory.create(
        menu_data["category"],
        menu_data["name"],
        menu_data["price"]
    )

def add_toppings(item, category):
    while True:
        available_toppings = show_toppings(category)
        if not available_toppings:
            return item

        topping_id = input_number(
            "Pilih topping: ",
            valid_options=[0, *available_toppings.keys()]
        )
        if topping_id == 0:
            return item

        topping = available_toppings[topping_id]
        item = MenuTopping(item, topping["name"], topping["price"])
        print(f"Topping ditambahkan: {item.get_name()}")

        if not input_yes_no("Tambah topping lagi? (y/n): "):
            return item

def create_order():
    print("==== KANTINKU ====")
    customer_name = input_text("Nama customer: ")

    order = OrderSubject(customer_name)
    order.attach(KitchenObserver())
    order.attach(CashierObserver())
    order.attach(DisplayObserver())

    while True:
        show_menu()
        menu_id = input_number("Pilih menu yang dipesan: ", valid_options=MENU_DB.keys())
        qty = input_number("Jumlah: ", minimum=1)

        menu_data = MENU_DB[menu_id]
        item = build_menu_item(menu_data)
        item = add_toppings(item, menu_data["category"])
        order.add_item(item, qty)

        print(f"{qty} x {item.get_name()} masuk ke order.")
        if not input_yes_no("Tambah pesanan lain? (y/n): "):
            break

    ORDER_DB[order.order_id] = order
    return order

def main():
    order = create_order()

    print("\n==== RINGKASAN ORDER ====")
    order.show_order()

    if input_yes_no("\nKonfirmasi order? (y/n): "):
        print("\nConfirm Order")
        order.confirm()

        if input_yes_no("\nTandai order selesai? (y/n): "):
            print("\nComplete Order")
            order.complete()
    else:
        print("Order belum dikonfirmasi.")

    print("\n==== DATABASE ORDER ====")
    print(f"Total order tersimpan: {len(ORDER_DB)}")


if __name__ == "__main__":
    main()
