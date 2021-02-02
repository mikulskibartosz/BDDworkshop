#Feature: Notify about new followers
#
#  #Rule: Send a notification when is followed by someone
#
#      Scenario: user receives notification about a new follower
#        Given Alice doesn't follow Bob
#        When Alice follows Bob
#        Then Bob gets a notification about a new follower