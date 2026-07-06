# Inventory Manager — Acceptance Testing with Behave (BDD)

Command-line application to manage products (add, list, update, remove, search)
validated through **acceptance tests** written in **Gherkin** and executed with
**Behave** (Behavior Driven Development).

## Requirements
- Python 3.x
- Behave (`pip install behave`)

## Setup
```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Run the application
```bash
python inventory.py
```

## Run the acceptance tests
```bash
behave
```

## Project structure
```
inventory-manager/
├── inventory.py              # CLI application (main file)
├── inventory_core.py         # Business logic (Product, Inventory)
├── requirements.txt
├── README.md
└── features/
    ├── environment.py        # Behave hooks (sys.path setup)
    ├── add_product.feature       # Feature 1
    ├── list_products.feature     # Feature 2
    ├── update_quantity.feature   # Feature 3
    ├── remove_product.feature    # Feature 4
    ├── search_product.feature    # Feature 5 (added)
    └── steps/
        └── inventory_steps.py    # Acceptance tests (step definitions)
```

## Features & Scenarios (5 + 5)
1. Add a product to the inventory
2. List all products in the inventory
3. Update the quantity of a product
4. Remove a product from the inventory
5. Search a product by name — failed interaction (added for the workshop)

## Product attributes (4)
`name`, `category`, `quantity`, `price`
