Feature: Log in feature

Background: Common steps for logging in
    Given User starts at login page
    Then User is able to see login and password inputs
    When User types proper credentials and proceed

Scenario: Successful login    
    Then The user can see a shop layout