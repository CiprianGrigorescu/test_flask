import json
from flask import request, current_app

from mathfunc.apis.math_pow.unmarshalling import MathFuncPowRequestSchema
from mathfunc.apis.math_pow.marshalling import MathFuncPowResultSchema
from mathfunc.models.requests import Requests
from mathfunc.app_main import db, cache


def get_math_pow():
    current_app.log.info('Start calculate POW')
    qs_args = MathFuncPowRequestSchema().load(request.args.to_dict(), unknown='EXCLUDE')
    # we can save it from MathFuncPowRequestSchema, using ModelSchema
    req = Requests(
        request_verb='GET',
        request_method='get_math_pow',
        request_params=json.dumps(qs_args)
    )
    try:
        db.session.add(req)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        current_app.log.info(f'Error saving req: {str(e)}')

    cache_key = f"{qs_args['number']}_{qs_args['power']}"
    res = cache.get(cache_key)
    if not res:
        res = pow(qs_args['number'], qs_args['power'])
        cache.set(cache_key, res, 300)

    result = {
        "result": res
    }
    return MathFuncPowResultSchema().dump(result)
