Feature: Users see their feed

  Rule: User's feed contains chunks posted by people followed by the user

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

  Rule: Users can retrieve their feed

       Scenario: Users see their own content
         Given Alice posted a chunk
         When Alice retrieves her own feed
         Then Alice sees the chunk

  Rule: Users see feeds of people they follow

     Scenario: Users see feeds of followed accounts
       Given Alice follows Bob
       And Bon posted a chunk
       When Alice retrieves Bob's feed
       Then Alice sees the chunk

  Rule: Users can see anyone's feeds

      Scenario: Users see all feeds
        Given Bob posted a chunk
        But Alice doesn't follow Bob
        When Alice retrieves Bob's feed
        Then Alice sees the content posted by Bob