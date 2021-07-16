def init_apis(connexion_app, api_services):
    """
    Initialize API routing

    :param connexion_app: Connexion App
    :param api_services: APIs list to expose
    :return:
    """

    for api in api_services:
        connexion_app.add_api(api['file'], base_path=api['base_path'], validate_responses=False, strict_validation=True)
