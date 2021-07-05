@todo
Feature: Todo list REST API

  Scenario: A tasks gets added to the list
    When a new task is added
    Then the list contains the task

  Scenario: A tasks gets completed
    Given a new tasks is added
    When the task gets completed
    Then the list does not contain the task
