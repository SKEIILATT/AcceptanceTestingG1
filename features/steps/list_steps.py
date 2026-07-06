"""
list_steps.py  --  PERSONA 4
------------------------------------------------------------
Steps del escenario "List all products in the inventory".
"""

from behave import when, then


@when('the user lists all products')
def step_impl(context):
    context.output = context.inventory.list_products()


@then('the output should contain:')
def step_impl(context):
    # context.text es el bloque de texto entre triple comillas del .feature
    expected = context.text.strip()
    assert expected in context.output, \
        f'Expected to find:\n{expected}\n--- but got: ---\n{context.output}'
