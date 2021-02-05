@lru
Feature: LRU list

  Scenario: an new list is empty
    When a new list is created
    Then the list is empty

  Scenario: the list contains an element
    Given a new list with max size "3" is created
    When a new element is added to the list
    Then the list contains "1" elements

  Scenario: the list contains all elements in order
    Given a new list with max size "3" is created
    When "3" elements are added to the list
    Then the list contains all added elements

  Scenario: the list drops old elements
    Given a new list with max size "2" is created
    When "3" elements are added to the list
    Then the list contains "2" elements
    And the first element is not in the list
    But two last elements are in the list