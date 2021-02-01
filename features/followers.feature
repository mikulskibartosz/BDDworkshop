Feature: Users can follow each other

  Rule: User can follow another user

      Scenario: user follows a new account
        Given Alice doesn't follow Bob
        When Alice follows Bob
        Then Bob is followed by Alice
        And Alice is a follower of Bob

  Rule: User can unfollow a follower

      Scenario: user can unfollow an account
        Given Alice follows Bob
        When Alice unfollows Bob
        Then Bob is not followed by Alice
        And Alice doesn't follow Bob