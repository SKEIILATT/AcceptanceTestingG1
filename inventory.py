"""
inventory.py
------------
Command-line interface for the Inventory Manager.

Run it with:
    python inventory.py

It offers a simple menu to add, list, update, remove and search products.
All the real work is delegated to the Inventory class in inventory_core.py,
which is the same class the acceptance tests exercise.
"""

from inventory_core import Inventory


MENU = """
============================================
        INVENTORY MANAGER
============================================
1. Add a product
2. List all products
3. Update the quantity of a product
4. Remove a product
5. Search a product by name
0. Exit
--------------------------------------------
Choose an option: """


def add_product(inv):
    name = input("Product name: ").strip()
    category = input("Category: ").strip() or "General"
    quantity = input("Quantity: ").strip() or "0"
    price = input("Price: ").strip() or "0"
    print(inv.add_product(name, category, int(quantity), float(price)))


def list_products(inv):
    print(inv.list_products())


def update_quantity(inv):
    name = input("Product name: ").strip()
    quantity = input("New quantity: ").strip() or "0"
    print(inv.update_quantity(name, int(quantity)))


def remove_product(inv):
    name = input("Product name: ").strip()
    print(inv.remove_product(name))


def search_product(inv):
    name = input("Product name: ").strip()
    print(inv.search_product(name))


def main():
    inv = Inventory()
    # A couple of sample products so the menu is not empty on first run.
    inv.add_product("Coffee", "Beverages", 10, 4.50)
    inv.add_product("Sugar", "Groceries", 20, 1.20)

    actions = {
        "1": add_product,
        "2": list_products,
        "3": update_quantity,
        "4": remove_product,
        "5": search_product,
    }

    while True:
        choice = input(MENU).strip()
        if choice == "0":
            print("Goodbye!")
            break
        action = actions.get(choice)
        if action:
            action(inv)
        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()
