"""
search_steps.py  --  PERSONA 4
------------------------------------------------------------
Steps del escenario "Search for a product that does not exist"
(la 5.a feature aniadida, interaccion fallida).
"""

from behave import when, then


@when('the user searches for the product "{product}"')
def step_impl(context, product):
    context.output = context.inventory.search_product(product)


@then('the output should be "{message}"')
def step_impl(context, message):
    assert context.output == message, \
        f'Expected "{message}" but got "{context.output}"'
