from functools import wraps
from flask import request, Response
from config import API_KEY


def failed_auth():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.headers.get('authorization')
        if not auth or auth != API_KEY:
            return failed_auth()
        return f(*args, **kwargs)
    return decorated