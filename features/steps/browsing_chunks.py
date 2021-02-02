import random
import string

from behave import *

from features.steps.api_client import *


def _random_string(n):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(n))


@given("Alice doesn\'t follow anyone")
def alice_unfollows_all(context):
    unfollow_all('Alice')


@when("Alice retrieves the feed")
def alice_retrieves_feed(context):
    context.feed = retrieve_chunks('Alice')


@then("Alice sees an empty list")
def feed_is_empty(context):
    print(context.feed)
    assert len(context.feed) == 0


@given("Alice follows Bob")
def alice_follows_bob(context):
    follow('Alice', 'Bob')


@given('Bob posted a chunk')
def bob_posts_chunk(context):
    context.expected_chunk = _random_string(20)
    post_chunk('Bob', context.expected_chunk)


@then('Alice sees the content posted by Bob')
def alice_sees_bob_post(context):
    filtered_feed = [x for x in context.feed if x['username'] == 'Bob' and x['chunk'] == context.expected_chunk]
    assert len(filtered_feed) == 1
