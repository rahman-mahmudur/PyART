import re

from webob.multidict import MultiDict
from cornice.validators._colander import (
    validator as colander_validator,
    body_validator as colander_body_validator,
    headers_validator as colander_headers_validator,
    path_validator as colander_path_validator,
    querystring_validator as colander_querystring_validator)
from cornice.validators._marshmallow import (
    validator as marshmallow_validator,
    body_validator as marshmallow_body_validator,
    headers_validator as marshmallow_headers_validator,
    path_validator as marshmallow_path_validator,
    querystring_validator as marshmallow_querystring_validator)


__all__ = ['colander_validator',
           'colander_body_validator',
           'colander_headers_validator',
           'colander_path_validator',
           'colander_querystring_validator',
           'marshmallow_validator',
           'marshmallow_body_validator',
           'marshmallow_headers_validator',
           'marshmallow_path_validator',
           'marshmallow_querystring_validator',
           'extract_cstruct',
           'DEFAULT_VALIDATORS',
           'DEFAULT_FILTERS']


DEFAULT_VALIDATORS = []
DEFAULT_FILTERS = []


def extract_cstruct(request):
    is_json = re.match('^application/(.*?)json$', str(request.content_type))

    if request.content_type in (
        'application/x-www-form-urlencoded',
        'multipart/form-data'
    ):
        body = request.POST.mixed()
    elif request.content_type and not is_json:
        body = request.body
    else:
        if request.body:
            try:
                body = request.json_body
            except ValueError as e:
                request.errors.add('body', '', 'Invalid JSON: %s' % e)
                return {}
            else:
                if not hasattr(body, 'items') and not isinstance(body, list):
                    request.errors.add('body', '',
                                       'Should be a JSON object or an array')
                    return {}
        else:
            body = {}

    cstruct = {'method': request.method,
               'url': request.url,
               'path': request.matchdict,
               'body': body}

    for sub, attr in (('querystring', 'GET'),
                      ('header', 'headers'),
                      ('cookies', 'cookies')):
        data = getattr(request, attr)
        if isinstance(data, MultiDict):
            reveal_type(data)