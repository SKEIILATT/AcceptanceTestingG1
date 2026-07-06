# language: en
Feature: Search a product by name
  As a store manager
  I want to search a product by its name
  So that I can quickly find out whether it exists in the inventory

  # This is the 5th feature/scenario added for the workshop.
  # It checks a FAILED interaction: searching for a product that
  # is not in the inventory must return a clear "not found" message.
  Scenario: Search for a product that does not exist
    Given the inventory contains products:
      | Product |
      | Sugar   |
    When the user searches for the product "Coffee"
    Then the output should be "Product Coffee was not found"
