import os
import uuid

import connexion
from dotenv import load_dotenv
from flask import g, request
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache

from mathfunc.utils.errors_manager import ErrorManager
from mathfunc.utils.logging_manager import LoggingManager

math_log = LoggingManager()
db = SQLAlchemy(
    session_options={
        'autoflush': False,
        'expire_on_commit': True
    }
)
cache = Cache(config={'CACHE_TYPE': 'MemcachedCache'})


def create_app(extra_config: dict = None):
    connexion_app = connexion.App(__name__, specification_dir='swagger/')
    flask_app = connexion_app.app

    load_dotenv(dotenv_path=os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), '.env'))
    flask_app.config.from_object('mathfunc.config.conf')
    if extra_config and isinstance(extra_config, dict):
        flask_app.config.update(extra_config)

    import mathfunc.apis as apis
    api_services = flask_app.config['API_SERVICES']
    apis.init_apis(connexion_app, api_services)

    ErrorManager.init_handle_exceptions(flask_app)
    math_log.init_logging(flask_app)
    db.init_app(flask_app)
    cache.init_app(flask_app)

    return flask_app


# Init Flask app
app = create_app()


@app.before_request
def before_request():
    """
    Init correlation id and logging before any request
    :return:
    """

    if not hasattr(g, 'correlation_id'):
        g.correlation_id = str(uuid.uuid4())
    # log the request
    math_log.set_request_logging(request)


@app.after_request
def after_request(response):
    """
    Init correlation id and logging before any request
    :return:
    """
    math_log.set_response_logging(request, response)
    return response
