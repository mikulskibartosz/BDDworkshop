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
        while {"from": user, "to": followed_user} in followers:
            followers.remove({"from": user, "to": followed_user})


def unfollow_all(user):
    with Persist('followers.json') as followers:
        for pair in followers:
            followers.remove(pair)


def profile(target_user, user):
    following = []
    followed_by = []
    with Persist('followers.json') as followers:
        for pair in followers:
            if pair['from'] == target_user:
                following.append(pair['from'])
            if pair['to'] == target_user:
                followed_by.append(pair['from'])

        return {'following': following, 'followed_by': followed_by}