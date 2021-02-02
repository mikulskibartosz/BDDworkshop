from bddtter.persist import Persist


def followed(username):
    with Persist('followers.json') as followers:
        return list(filter(lambda x: x["from"] == username, followers))


def follow(followed_user, user):
    with Persist('followers.json') as followers:
        if (user, followed_user) not in followers:
            followers.append({"from": user, "to": followed_user})


def unfollow(followed_user, user):
    with Persist('followers.json') as followers:
        followers.remove({"from": user, "to": followed_user})


def unfollow_all(user):
    with Persist('followers.json') as followers:
        for pair in followers:
            followers.remove(pair)
