import random
import string

from behave import *

from features.steps.api_client import *


def _random_string(n):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(n))


@when("Alice retrieves the feed")
def alice_retrieves_feed(context):
    context.feed = retrieve_chunks('Alice')


@then("Alice sees an empty list")
def feed_is_empty(context):
    print(context.feed)
    assert len(context.feed) == 0


@given('Bob posted a chunk')
def bob_posts_chunk(context):
    context.expected_chunk = _random_string(20)
    post_chunk('Bob', context.expected_chunk)


@then('Alice sees the content posted by Bob')
def alice_sees_bob_post(context):
    filtered_feed = [x for x in context.feed if x['username'] == 'Bob' and x['chunk'] == context.expected_chunk]
    assert len(filtered_feed) == 1


@then("Alice doesn\'t see the content posted by Bob")
def alice_doesnt_see_bob_post(context):
    print(context.feed)
    filtered_feed = [x for x in context.feed if x['username'] == 'Bob' and x['chunk'] == context.expected_chunk]
    assert len(filtered_feed) == 0


@when('Bob retrieves his own feed')
def bob_retrives_own_feed(context):
    context.feed = retrieve_user_feed('Bob')


@then('Bob sees the chunk posted by himself')
def bob_sees_his_post(context):
    print(context.feed)
    filtered_feed = [x for x in context.feed if x['username'] == 'Bob' and x['chunk'] == context.expected_chunk]
    assert len(filtered_feed) == 1