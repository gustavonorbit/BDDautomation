

Feature: Verifying registration functionality

    Scenario: registration with valid data
    Given User is on registration page
    When User enters username
    And User enters email id
    And User enters password
    And User Click on signup button
    Then User should be registered successfully

   