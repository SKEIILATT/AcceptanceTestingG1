"""
add_steps.py  --  PERSONA 3
------------------------------------------------------------
Steps del escenario "Add a product to the inventory".
"""

from behave import when, then


@when('the user adds a product "{product}"')
def step_impl(context, product):
    context.output = context.inventory.add_product(product)


@then('the inventory should contain "{product}"')
def step_impl(context, product):
    assert context.inventory.contains(product), \
        f'Product "{product}" not found in the inventory'
