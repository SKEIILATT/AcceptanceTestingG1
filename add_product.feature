# language: en
Feature: Add a product to the inventory
  As a store manager
  I want to add products to the inventory
  So that I can keep track of the stock I have available

  Scenario: Add a product to the inventory
    Given the inventory is empty
    When the user adds a product "Coffee"
    Then the inventory should contain "Coffee"
