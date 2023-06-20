Feature: Log in feature 

Scenario: Successful login  
    Given User starts at login page
    When User types proper credentials and proceed
    Then The user can see a shop layout

Scenario: Wrong email
    Given User starts at login page
    When User types wrong e-mail and right password and proceed
    Then User should see error field with error message