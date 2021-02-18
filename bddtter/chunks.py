from followers import followed
from persist import Persist
import connexion


def _get_user_feed(user):
    followed_by_user = list(map(lambda x: x["to"], followed(user)))
    with Persist('chunks.json') as chunks:
        return [chunk for chunk in chunks if chunk['username'] in followed_by_user]


def read(user):
    return _get_user_feed(user)


def read_user_feed(target_user, user):
    with Persist('chunks.json') as chunks:
        return [chunk for chunk in chunks if chunk['username'] in target_user]


def post(user):
    chunk = connexion.request.json['chunk']
    with Persist('chunks.json') as chunks:
        chunks.append({
            "username": user,
            "chunk": chunk,
            "timestamp": 'datetime.now()'
        })
