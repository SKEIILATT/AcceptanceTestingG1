"""
environment.py
--------------
Behave hooks. Ensures the project root is importable so that
`from inventory_core import Inventory` works when running `behave`.
"""
import os
import sys

# Add the project root (one level up from the features folder) to sys.path.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
