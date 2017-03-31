import functools

import flask


def trace(f):
    @functools.wraps(f)
    def decorated(*args, **kwargs):
        root_span = getattr(flask.g, '_zipkin_span', None)
        if root_span is not None:
            with root_span:
                return f(*args, **kwargs)

    return decorated
