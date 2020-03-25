import json as js
import functools


def to_json(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        res = js.dumps(func(*args, **kwargs))
        return res

    return wrapped

