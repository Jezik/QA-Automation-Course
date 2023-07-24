Feature: Firt steps with test data generation

Scenario: Moccaro
    Given User send proper request to Moccaro
    Then Request return with proper status code
    When User picks address from json
    Then Correct address should be printed out

Scenario: Faker
    Given User generates some data with Faker
    Then Generated data is saved in a .json file inside test_data folder
    And Address value from .json file is printed out
