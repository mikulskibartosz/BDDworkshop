import requests


def _make_url(resource):
    return f'http://0.0.0.0:5000/api/{resource}'


def retrieve_chunks(username):
    response = requests.get(_make_url('chunks'), auth=(username, 'pass'))
    return response.json()


def retrieve_user_feed(username):
    response = requests.get(_make_url(f'chunks/{username}'), auth=(username, 'pass'))
    return response.json()


def post_chunk(username, chunk):
    requests.post(_make_url('chunks'), json={'chunk': chunk}, auth=(username, 'pass'))


def follow(username, followed_user):
    requests.put(_make_url(f'following/{followed_user}'), auth=(username, 'pass'))


def unfollow(username, followed_user):
    requests.delete(_make_url(f'following/{followed_user}'), auth=(username, 'pass'))


def unfollow_all(username):
    requests.delete(_make_url('following'), auth=(username, 'pass'))


def profile(target_user, username):
    response = requests.get(_make_url(f'profile/{target_user}'), auth=(username, 'pass'))
    return response.json()
