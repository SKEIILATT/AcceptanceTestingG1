"""
update_steps.py  --  PERSONA 5
------------------------------------------------------------
Steps del escenario "Update the quantity of a product".
"""

from behave import when, then


@when('the user updates product "{product}" to quantity "{quantity}"')
def step_impl(context, product, quantity):
    context.output = context.inventory.update_quantity(product, int(quantity))


@then('the inventory should show product "{product}" with quantity "{quantity}"')
def step_impl(context, product, quantity):
    product_obj = context.inventory.get_product(product)
    assert product_obj is not None, f'Product "{product}" not found'
    assert product_obj.quantity == int(quantity), \
        f'Expected quantity {quantity} but got {product_obj.quantity}'
