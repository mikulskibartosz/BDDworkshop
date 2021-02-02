import connexion


def basic_auth(username, password, required_scopes=None):
    return {'sub': username}  # we should check the password here, but it is an example so let's accept all


if __name__ == '__main__':
    app = connexion.FlaskApp(__name__,)
    app.add_api('swagger.yml')
    app.run(host='0.0.0.0', port=5000, debug=True)
