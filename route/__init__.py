from flask import Blueprint
routes = Blueprint('routes', __name__)

from .index import *
from .before_request import *
from .error import *
