"""
remove_steps.py  --  PERSONA 6
------------------------------------------------------------
Steps del escenario "Remove a product from the inventory".
"""

from behave import when, then


@when('the user removes the product "{product}"')
def step_impl(context, product):
    context.output = context.inventory.remove_product(product)


@then('the inventory should not contain "{product}"')
def step_impl(context, product):
    assert not context.inventory.contains(product), \
        f'Product "{product}" is still in the inventory'
