from connexion.exceptions import OAuthScopeProblem, Unauthorized


def basic_auth(username, password, required_scopes=None):
    if username == 'admin' and password == 'admin':
        info = {'sub': 'admin', 'scope': 'read'}
    else:
        # optional: raise exception for custom error response
        raise Unauthorized('Not allowed')

    # optional
    if required_scopes is not None and required_scopes != info['scope']:
        raise OAuthScopeProblem(
                description='Provided user doesn\'t have the required access rights',
                required_scopes=required_scopes,
                token_scopes=info['scope']
            )

    return info
