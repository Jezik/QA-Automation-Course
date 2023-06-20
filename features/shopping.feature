Feature: Add item to cart feature

Scenario: First item add to cart
    Given User starts at login page
    When User types proper credentials and proceed
    Then The user can see a shop layout
    When The user click on add to cart button
    Then The item adds to cart and the cart icon shows the number 1
