# language: en
Feature: List all products in the inventory
  As a store manager
  I want to list every product in the inventory
  So that I can see the complete stock at a glance

  Scenario: List all products in the inventory
    Given the inventory contains products:
      | Product |
      | Coffee  |
      | Sugar   |
    When the user lists all products
    Then the output should contain:
      """
      Products:
      - Coffee
      - Sugar
      """
