import random
import string

from behave import *

from lru import LRU


def _random_string(n):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(n))


@given('a new list with max size "{list_size:d}" is created')
def create_new_list(context, list_size):
    context.object_under_test = LRU(list_size)


@when('a new list is created')
def create_new_list(context):
    context.execute_steps(u"""
        given a new list with max size "1" is created
    """)


@when(u'a new element is added to the list')
def add_new_element(context):
    random_text = _random_string(20)
    if 'added_values' in context:
        context.added_values.append(random_text)
    else:
        context.added_values = [random_text]

    context.object_under_test += random_text


@when('"{number_of_elements:d}" elements are added to the list')
def add_n_elements(context, number_of_elements):
    for _ in range(0, number_of_elements):
        context.execute_steps(u"""
            when a new element is added to the list
        """)


@then('the list is empty')
def assert_list_empty(context):
    assert len(context.object_under_test) == 0


@then(u'the list contains "{number_of_elements:d}" elements')
def assert_list_length(context, number_of_elements):
    assert len(context.object_under_test) == number_of_elements


@then('the list contains all added elements')
def assert_list_content(context):
    actual = [x for x in context.object_under_test]
    assert actual == context.added_values


@then(u'the first element is not in the list')
def step_impl(context):
    actual = [x for x in context.object_under_test]
    first_element = context.added_values[0]
    assert first_element not in actual


@then(u'two last elements are in the list')
def step_impl(context):
    actual = [x for x in context.object_under_test]
    expected_elements = context.added_values[1:]
    assert actual == expected_elements
