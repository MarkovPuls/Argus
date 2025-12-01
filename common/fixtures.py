from datetime import datetime
from functools import wraps
import logging

logger = logging.getLogger('Fixture')


def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        response = func(*args, **kwargs)
        duration_ms = (datetime.now() - start_time).total_seconds() * 1000
        response.time = duration_ms
        logger.info(f"Request {func.__name__} занял: {duration_ms:.2f} ms")
        return response
    return wrapper


def log_request(method_name: str):
    def decorator(func):
        @wraps(func)
        def wrapper(self, url, *args, **kwargs):
            body = kwargs.get('json') or kwargs
            logger.info(f'REQUESTS {method_name} → {url} | params/body={body}')
            res = func(self, url, *args, **kwargs)
            logger.info(f'RESPONSE ← {res.code} {res.status} | url={url}')
            return res
        return wrapper
    return decorator

