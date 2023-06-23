Feature: WebDriverUniversity farther testing

Scenario: First look at attributes
    Given User opened the page for attributes testing
    When User click plus sign
    Then The class attribute of a button should change to correct one

Scenario: Checkboxes
    Given User opened the page for Checkboxes
    Then The field Cabbage should be disabled

Scenario: Dropdown
    Given User opened the page for Checkboxes
    When User openes the first menu item and selects Python
    Then User should see the Python in a first dropdown item

Scenario: Waiting
    Given User opened a page with spinner
    When The wait is over
    Then The user should see a button
    When The user clicks on this button
    Then The correct text should be shown

Scenario: Image upload
    Given User opened a page for image uploading
    When User uploads an image
    When User clicks on upload button
    Then The popup with success message appears
