from behave import *
from todo.api_client import *

@when(u'a new task is added')
def add_new_task(context):
    context.task = {'content': 'task content'}
    add_task(context.task)


@then(u'the list contains the task')
def assert_list_contains_the_task(context):
    all_tasks = get_tasks()
    found = list(filter(lambda x: x['content'] == context.task['content'], all_tasks))
    assert found


@given(u'a new tasks is added')
def step_impl(context):
    context.execute_steps(u"when a new task is added")


@when(u'the task gets completed')
def step_impl(context):
    all_tasks = get_tasks()
    context.task_id = all_tasks[0]['id']
    complete_task(context.task_id)


@then(u'the list does not contain the task')
def step_impl(context):
    all_tasks = get_tasks()
    found = list(filter(lambda x: x['id'] == context.task_id, all_tasks))
    print(found)
    assert not found
