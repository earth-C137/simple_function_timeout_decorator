from multiprocessing.pool import ThreadPool

# timeout is in seconds
def timeout_decorator(func, timeout=1):
    def wrapper(*args):
        pool = ThreadPool(processes=1)
        result = pool.apply_async(func, (*args,))
        val = result.get(timeout=timeout)
        return val
    return wrapper
