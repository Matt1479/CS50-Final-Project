from flask import redirect, session
from functools import wraps

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif', 'webp', 'bmp'])

def login_required(f):
    """Decorate routes to require login"""

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    
    return decorated_function

def sulogin_required(f):
    """Decorate superuser routes to require login"""

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("su_id") is None:
            return redirect("/sulogin")
        return f(*args, **kwargs)
    
    return decorated_function


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS