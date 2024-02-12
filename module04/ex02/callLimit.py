from functools import wraps


def callLimit(limit: int):
    count = 0

    def callLimiter(function):
        @wraps(function)
        def limit_function(*args: any, **kwds: any):
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print(f"Function {function.__name__} called too many times.")
        return limit_function
    return callLimiter
