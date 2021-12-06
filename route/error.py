from flask import Flask
from flask import make_response,Flask,session,request,abort
from . import routes
@routes.errorhandler(403)
@routes.errorhandler(500)
def server_error(e):
  return 'an error occurred.', e.code