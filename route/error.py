
from . import routes


@routes.errorhandler(403)
@routes.errorhandler(500)
def server_error(e):
    return 'an error occurred.', e.code
