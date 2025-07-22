Feature: Verifying registration functionality

    Scenario: Registration with valid data
    Given User is on Registrattion page
    When User enter username
    And User enter password
    And User click on signup button
    Then User should be registered successfully

    Scenario: Registration with duplicate username data
    Given User is on Registrattion page
    When User enter username
    And User enter password
    And User click on signup button
    Then User should be registered successfully