#Feature: Posting new content
#
#    #Rule: Logged in user should be able to post new content
#
#    Scenario: user posts new content
#        Given user has valid session token
#        When user posts a new chunk
#        Then the chunk is visible in users's personal feed
#
#    #Rule: Not logged-in user attempts to post new content
#
#    Scenario: not logged in user posts new content
#        Given user is not logged in
#        When user posts a new chunk
#        Then user receives access error
#        And the new chunk is not added to user's personal feed