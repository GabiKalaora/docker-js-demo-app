# Created by Gabi at 14/09/2021
Feature: Edit profile in app to edit profile and check if data really changed

  Scenario: Edit profile
    Given The profile has: name "Anna Smith" ,email "anna.smith@example.com", interests "coding"
    When To edit to:     'name': 'Gabi','email': 'GabiDaCoder@gmail.com','interests': 'Coding / Debugging'
    Then DB will hold new info
