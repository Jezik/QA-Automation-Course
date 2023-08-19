Feature: Mobile testing 

Scenario: Open mobile
    Given Open google on mobile
    Then Check url

Scenario: Chromedriver mobile page
    Given User opens chromedriver url on mobile device
    When User closes cookies popup
    And User opens 'hamburger menu'
    Then First three links should be visible
    When User rolls down 'Downloads' link
    And User clicks on 'version selection' link
    Then User should be on 'https://chromedriver.chromium.org/downloads/version-selection' page
    When User scrolls down till the bottom
    Then The correct text should be visible to user
