Feature: First steps with api testing
@wip
Scenario: Perform GET request and use part of the response in a POST request
    Given User perform GET request to a https://jsonplaceholder.typicode.com/users with username=Antonette
    When User takes id from the response and use it in the POST request
    Then The server response should contain correct data
