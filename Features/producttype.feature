Feature: Product Type Navigation
  As a registered user
  I want to navigate to the product type by clicking on the "Add New" button in the listing
  So that I can manage product types easily

  Background:
    Given the user is on the login page
    When the admin enters valid username and password
    Then the user should either be successfully logged in or see the another session page
    And user chooses Admin from product selection

  Scenario: User navigates to Product type Listing from the admin panel
    Given the user is on the admin panel
    When the user clicks on the "Product Types" option in the side menu
    Then the user should be redirected to the "Product Type" page


  Scenario: User navigates to add Add Product type from the admin panel
    Given the user is on the admin panel
    When the user clicks on the "Product Types" option in the side menu
    And  the user clicks on "Add New Product Type" button
    Then the user should be redirected to the "Add Product Type" page


  Scenario: User creates a product type by adding all the required fields
    Given the user is on the admin panel
    When the user clicks on the "Product Types" option in the side menu
    And  the user clicks on "Add New Product Type" button
    And the user add all required fields
    And the user clicks on the "Save" button
    Then the new product type is successfully created
    And the user sees a success message confirming the creation


  Scenario: User creates a product type by adding all the required fields
    Given the user is on the admin panel
    When the user clicks on the "Product Types" option in the side menu
    And  the user clicks on "Add New Product Type" button
    And the user add all required fields
    And the user clicks on the "Save" button
    Then the new product type is successfully created
    And the user is able to see the product in listing



  @undertest

  Scenario: User edits a product type and observes the updated name in the product list

    Given the user is on the admin panel
    When the user clicks on the "Product Types" option in the side menu
    And  the user clicks on "Add New Product Type" button
    And the user add all required fields
    And the user clicks on the "Save" button
    And the user selects an added product type from the list
    And the user updates the name of the product type
    Then the product type is successfully updated
    And the user is redirected to the product type listing to see the updated result

