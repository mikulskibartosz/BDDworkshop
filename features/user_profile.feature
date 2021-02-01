Feature: Every user has a personal profile

  Rule: User creates a new profile

      Scenario: user creates a profile
        Given user picks a not existing username
        When user creates a new profile
        Then the profile is created

      Scenario: user cannot create a profile with an existing name
        Given the username already exists
        When user creates a new profile
        Then user gets NotAvailable error

  Rule: Profile contains all user information

      Scenario: retrieved user profile contains followers and followed accounts
        When user retrieves own profile
        Then the profile contains followed accounts
        And the profile contains accounts who follow the user