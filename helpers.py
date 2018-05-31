from timeit import default_timer
from time import sleep


def timer(verbose=True):
    def inner(func):
        def wrapper(*args, **kwargs):
            started = default_timer()
            result = func(*args, **kwargs)
            delta = default_timer() - started
            if verbose:
                print("Runned: %(func)s, elapsed: %(delta)f s" %
                    {'func': func, 'delta': delta})
            return result
        return wrapper
    return inner

if __name__ == '__main__':
    @timer(verbose=True)
    def tester():
        print("Run tester")
        for i in range(1000):
            res = 2**i

    tester()

