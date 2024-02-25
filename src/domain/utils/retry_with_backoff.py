import time
from functools import wraps

class RetryLimitExceededException(Exception):
    def __init__(self, last_exception):
        self.last_exception = last_exception
        super().__init__(f"Retry limit exceeded. Last exception: {last_exception}")

def retry_with_backoff(retries=3, backoff_in_seconds=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal backoff_in_seconds
            attempts = 0
            last_exception = None
            while attempts < retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    attempts += 1
                    if attempts == retries:
                        raise RetryLimitExceededException(last_exception) from e
                    time.sleep(backoff_in_seconds)
                    backoff_in_seconds += 1
                    print(f"Retry {attempts}/{retries} after exception: {e}. Backing off for {backoff_in_seconds} seconds.")
        return wrapper
    return decorator
