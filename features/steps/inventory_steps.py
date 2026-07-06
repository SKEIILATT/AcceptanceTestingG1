"""
inventory_steps.py
------------------
Behave step definitions for the Inventory Manager acceptance tests.

Each step matches a line written in the .feature files (Gherkin) and
runs the corresponding logic from inventory_core.Inventory.

We store the inventory on Behave's `context` object. Behave creates a
fresh context for every scenario, so data never leaks between scenarios.
"""

from behave import given, when, then
from inventory_core import Inventory


# =====================================================================
# GIVEN  ->  put the system in a known state (pre-conditions)
# =====================================================================

@given('the inventory is empty')
def step_impl(context):
    context.inventory = Inventory()


@given('the inventory contains products:')
def step_impl(context):
    # The data comes from the Gherkin table, read by Behave as context.table.
    context.inventory = Inventory()
    for row in context.table:
        name = row['Product']
        if 'Quantity' in row.headings:
            context.inventory.add_product(name, quantity=int(row['Quantity']))
        else:
            context.inventory.add_product(name)


# =====================================================================
# WHEN  ->  the action the user performs
# =====================================================================

@when('the user adds a product "{product}"')
def step_impl(context, product):
    context.output = context.inventory.add_product(product)


@when('the user lists all products')
def step_impl(context):
    context.output = context.inventory.list_products()


@when('the user updates product "{product}" to quantity "{quantity}"')
def step_impl(context, product, quantity):
    context.output = context.inventory.update_quantity(product, int(quantity))


@when('the user removes the product "{product}"')
def step_impl(context, product):
    context.output = context.inventory.remove_product(product)


@when('the user searches for the product "{product}"')
def step_impl(context, product):
    context.output = context.inventory.search_product(product)


# =====================================================================
# THEN  ->  the observable outcome (assertions)
# =====================================================================

@then('the inventory should contain "{product}"')
def step_impl(context, product):
    assert context.inventory.contains(product), \
        f'Product "{product}" not found in the inventory'


@then('the output should contain:')
def step_impl(context):
    # context.text holds the triple-quoted docstring from the feature file.
    expected = context.text.strip()
    assert expected in context.output, \
        f'Expected to find:\n{expected}\n--- but got: ---\n{context.output}'


@then('the inventory should show product "{product}" with quantity "{quantity}"')
def step_impl(context, product, quantity):
    product_obj = context.inventory.get_product(product)
    assert product_obj is not None, f'Product "{product}" not found'
    assert product_obj.quantity == int(quantity), \
        f'Expected quantity {quantity} but got {product_obj.quantity}'


@then('the inventory should not contain "{product}"')
def step_impl(context, product):
    assert not context.inventory.contains(product), \
        f'Product "{product}" is still in the inventory'


@then('the output should be "{message}"')
def step_impl(context, message):
    assert context.output == message, \
        f'Expected "{message}" but got "{context.output}"'
