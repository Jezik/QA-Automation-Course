Feature: Mock testing on https://webdriveruniversity.com

Scenario: Add 2 tasks into To-Do list
    Given User has opened the page with to-do list
    Then User can see 3 default tasks in a list
    When User adds 2 more tasks in a list
    Then List should contains 5 tasks with correct names

Scenario: Mark all default tasks as done
    Given User has opened the page with to-do list
    Then User can see 3 default tasks in a list
    When User marks all 3 default tasks as done
    Then All default tasks should become strikethrough

Scenario: Deleting 2 tasks
    Given User has opened the page with to-do list
    Then User can see 3 default tasks in a list
    When User removes the 1st and the 3rd tasks
    Then List contains only the 2nd default task

Scenario: iFrame playground
    Given User has opened the page with iFrame
    Then User should be able to see three headers Who we are? Why Choose us? Greate service!
