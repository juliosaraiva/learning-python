from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'Ran in: {t2 - t1}')
        return result

    return wrapper


@performance
def long_time():
    x = 1
    while x < 1000000:
        print(x)
        x *= 5


long_time()
