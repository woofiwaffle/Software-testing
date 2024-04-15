Feature: Login
   In order to access my account
   As a registered user
   I want to be able to login

   Scenario: Successful login with correct credentials
      Given I am on the login page
      When I enter my username and password
      And click the login button
      Then I should be redirected to the homepage