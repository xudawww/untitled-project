
from flask import session, request, abort
from . import routes


@routes.before_request
def csrf_protect():
    if request.method == "POST":
        print(session)
        if session['_csrf_token']:
            token = session['_csrf_token']

        if not token or token != request.headers.get('X-XSRF-TOKEN'):
            abort(403)
