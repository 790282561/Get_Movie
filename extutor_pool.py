from functools import wraps
from concurrent.futures import ThreadPoolExecutor

a = [x for x in range(1001)]


def foo(n):
    print(str(n)[-1])


pool2 = ThreadPoolExecutor(100)
pool2.map(foo, a)
