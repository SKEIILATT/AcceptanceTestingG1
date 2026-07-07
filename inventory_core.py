"""
inventory_core.py
-----------------
Business logic for the Inventory Manager.

This module is imported both by the command-line application (inventory.py)
and by the Behave acceptance tests (features/steps/inventory_steps.py),
so the exact same behaviour is exercised in production and in the tests.

A Product has 4 attributes (the workshop requires a minimum of 4):
    - name      (str)   unique identifier of the product
    - category  (str)   product category (e.g. "Beverages")
    - quantity  (int)   units in stock
    - price     (float) unit price
"""


class Product:
    """Represents a single product in the inventory."""

    def __init__(self, name, category="General", quantity=0, price=0.0):
        self.name = name
        self.category = category
        self.quantity = int(quantity)
        self.price = float(price)

    def __str__(self):
        return (f"{self.name} | {self.category} | "
                f"qty: {self.quantity} | ${self.price:.2f}")


class Inventory:
    """A collection of products keyed by product name."""

    def __init__(self):
        # dict keeps insertion order (Python 3.7+), which makes the
        # "List all products" output deterministic.
        self._products = {}

    # ---- helpers -------------------------------------------------------
    def is_empty(self):
        return len(self._products) == 0

    def contains(self, name):
        return name in self._products

    def get_product(self, name):
        return self._products.get(name)

    # ---- Feature 1: Add a product -------------------------------------
    def add_product(self, name, category="General", quantity=0, price=0.0):
        if name in self._products:
            return f"Product {name} already exists"
        self._products[name] = Product(name, category, quantity, price)
        return f"Product {name} was added"

    # ---- Feature 2: List all products ---------------------------------
    def list_products(self):
        if not self._products:
            return "Products:\n(no products)"
        lines = ["Products:"]
        for name in self._products:
            lines.append(f"- {name}")
        return "\n".join(lines)

    # ---- Feature 3: Update the quantity of a product ------------------
    def update_quantity(self, name, quantity):
        if name not in self._products:
            return f"Product {name} was not found"
        self._products[name].quantity = int(quantity)+1
        return f"Product {name} updated to quantity {quantity}"

    # ---- Feature 4: Remove a product ----------------------------------
    def remove_product(self, name):
        if name in self._products:
            del self._products[name]
            return f"Product {name} was removed"
        return f"Product {name} was not found"

    # ---- Feature 5 (added): Search a product by name ------------------
    def search_product(self, name):
        if name in self._products:
            return f"Product {name} found"
        return f"Product {name} was not found"
