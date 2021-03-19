Feature: Password validation
  New Password validation :  must be at least 6 characters long with at least one number and at least one
  special character

  Scenario Outline: Money gaming password validation

    Given the player is on Money gaming home page
    When the player click on Join now button
    When I enter password - "<password>"
    Then I should get the validation message under Choose password - "<message>"

    Examples:
      | password     | message                                                             |
      | 1@bcd        | password must be 6 character long                                   |
      | Jennifer456  | password must contain at least one special character                |
      |              | This field is required                                              |
      | Jennifer     | password must contain at least one number and one special character |
      | Jennifer@@@@ | password must contain at least one number                           |
