"""
common_steps.py  --  PERSONA 2
------------------------------------------------------------
Steps COMPARTIDOS (los "Given"). Estos preparan el inventario
antes de cada escenario y son usados por varias features, por eso
van en UN SOLO archivo para no duplicarlos.
NO copies estos "Given" en los otros archivos de steps.
"""

from behave import given
from inventory_core import Inventory


@given('the inventory is empty')
def step_impl(context):
    context.inventory = Inventory()


@given('the inventory contains products:')
def step_impl(context):
    # Los datos vienen de la tabla Gherkin (context.table).
    context.inventory = Inventory()
    for row in context.table:
        name = row['Product']
        if 'Quantity' in row.headings:
            context.inventory.add_product(name, quantity=int(row['Quantity']))
        else:
            context.inventory.add_product(name)
