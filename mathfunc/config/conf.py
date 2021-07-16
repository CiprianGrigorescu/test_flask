import os

# used if we have diff versions: v1, v2 etc
API_SERVICES = [
    {"base_path": "", "file": "api.yaml"}
]
BASE_PATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
LOGGING_DIR = os.path.join(BASE_PATH, 'logs')
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS', False)
