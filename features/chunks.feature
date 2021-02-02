Feature: Users post chunks

  #Rule: User's feed contains chunks posted by people followed by the user

      Scenario: User who doesn't follow anyone doesn't see chunks
        Given Alice doesn't follow anyone
        When Alice retrieves the feed
        Then Alice sees an empty list

      Scenario: User sees chunks posted by followed accounts
        Given Alice follows Bob
        And Bob posted a chunk
        When Alice retrieves the feed
        Then Alice sees the content posted by Bob

      Scenario: User does not see content posted by strangers
        Given Bob posted a chunk
        But Alice doesn't follow Bob
        When Alice retrieves the feed
        Then Alice doesn't see the content posted by Bob

  #Rule: Users can retrieve their feed

       Scenario: Users see their own content
         Given Bob posted a chunk
         When Bob retrieves his own feed
         Then Bob sees the chunk posted by himself
