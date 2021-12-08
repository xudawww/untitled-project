
from flask import make_response, render_template, session
import uuid
from . import routes


@routes.route("/")
def hello_world():
    response = make_response(render_template("index.html"))
    response.set_cookie('XSRF-TOKEN', generate_csrf_token())
    return response


def generate_csrf_token():
    if '_csrf_token' not in session:
        session['_csrf_token'] = str(uuid.uuid4())
    return session['_csrf_token']
