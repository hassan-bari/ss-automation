Feature: Product Type Navigation
  As a registered user
  I want to navigate to the product type by clicking on the "Add New" button in the listing
  So that I can manage product types easily

  Background:
    Given the user is on the login page
    When the admin enters valid username and password
    Then the user should either be successfully logged in or see the another session page

  Scenario: User navigates to add product type from the admin panel
    Given the user is on the admin panel
    When the user clicks on the "Product Types" option in the side menu
    And the user clicks on the "Add New" button
    Then the user should be redirected to the "Add Product Type" page
