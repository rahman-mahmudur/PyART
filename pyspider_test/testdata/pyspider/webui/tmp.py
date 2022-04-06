import random
try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode

from flask import request
from .app import app


@app.route('/bench')
def bench_test():
    total = int(request.args.get('total', 10000))
    show = int(request.args.get('show', 20))
    nlist = [random.randint(1, total) for _ in range(show)]
    result = []
    args = dict(request.args)
    for nl in nlist:
        args['n'] = nl
        reveal_type(args)