# language: en
Feature: Remove a product from the inventory
  As a store manager
  I want to remove a product from the inventory
  So that discontinued products no longer appear in the stock

  Scenario: Remove a product from the inventory
    Given the inventory contains products:
      | Product |
      | Coffee  |
      | Sugar   |
    When the user removes the product "Coffee"
    Then the inventory should not contain "Coffee"
