Feature: Add item to cart feature

Background: Common steps for logging in
    Given User starts at login page
    Then User is able to see login and password inputs
    When User types proper credentials and proceed

Scenario: First item add to cart
    Then The user can see a shop layout
    When The user click on add to cart button
    Then The item adds to cart and the cart icon shows the number 1
