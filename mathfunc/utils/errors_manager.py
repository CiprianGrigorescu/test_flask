from connexion.exceptions import ConnexionException, BadRequestProblem, ProblemException, ResolverProblem
from werkzeug.exceptions import HTTPException, InternalServerError, NotFound, Unauthorized, Forbidden
from marshmallow.exceptions import MarshmallowError
from flask import jsonify, g


API_EXCEPTIONS = [
    ConnexionException,
    BadRequestProblem,
    ProblemException,
    ResolverProblem,
    HTTPException,
    InternalServerError,
    NotFound,
    Unauthorized,
    Forbidden,
    MarshmallowError
]


class ErrorManager:

    ERROR_CODES = {
        400: "Bad Request",
        401: "Unauthorized",
        403: "Forbidden",
        404: "Not Found"

    }

    @classmethod
    def init_handle_exceptions(cls, app):
        app.register_error_handler(InternalServerError, lambda error: cls._handle_exception(error))
        # any 500 exception
        app.register_error_handler(500, lambda error: cls._handle_exception(error))
        for exc in API_EXCEPTIONS:
            app.register_error_handler(exc, lambda error: cls._handle_exception(error))

    @staticmethod
    def _handle_exception(exception: Exception) -> dict:
        if hasattr(exception, 'status_code'):
            status_code = exception.status_code
        elif hasattr(exception, 'code'):
            status_code = exception.code
        else:
            status_code = 500

        if hasattr(exception, 'description'):
            msg = exception.description
        elif hasattr(exception, 'message'):
            msg = exception.message
        else:
            msg = f"{type(exception).__name__}: {str(exception)}"

        error = {
            'error_id': g.get('correlation_id', ''),
            'message': msg,
            'code': status_code
        }
        return jsonify(error)
