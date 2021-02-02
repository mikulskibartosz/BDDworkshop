from behave import *

from features.steps.api_client import *


@given("Alice doesn\'t follow anyone")
def alice_unfollows_all(context):
    unfollow_all('Alice')


@given("Alice follows Bob")
def alice_follows_bob(context):
    follow('Alice', 'Bob')


@when("Alice follows Bob")
def alice_follows_bob(context):
    follow('Alice', 'Bob')


@given("Alice doesn't follow Bob")
def alice_unfollows_bob(context):
    unfollow('Alice', 'Bob')


@then('Bob is followed by Alice')
def bob_profile_contains_follower_alice(context):
    profile_content = profile('Bob', 'Bob')
    print(profile_content)
    followed_by = profile_content['followed_by']
    assert 'Alice' in followed_by


@then('Alice is a follower of Bob')
def alice_profile_contains_following_bob(context):
    profile_content = profile('Alice', 'Bob')
    print(profile_content)
    following = profile_content['following']
    assert 'Alice' in following


@when(u'Alice unfollows Bob')
def step_impl(context):
    unfollow('Alice', 'Bob')


@then(u'Bob is not followed by Alice')
def step_impl(context):
    profile_content = profile('Bob', 'Bob')
    print(profile_content)
    followed_by = profile_content['followed_by']
    assert 'Alice' not in followed_by


@then(u'Alice doesn\'t follow Bob')
def step_impl(context):
    profile_content = profile('Alice', 'Bob')
    print(profile_content)
    following = profile_content['following']
    assert 'Alice' not in following
