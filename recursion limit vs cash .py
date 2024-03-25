from functools import lru_cache
import time
from sys import *

def cash():
    @lru_cache(maxsize=None, typed=False)
    def f(n):
        if n<3:
            return 3
        else:
            return 2*n+5+f(n-2)
    for x in range(1,300027):
        f(x)
    f(300027)-f(300023)
def recursion():
    setrecursionlimit(300027)
    def f(n):
        if n<3:
            return 3
        else:
            return 2*n+5+f(n-2)
    f(300027) - f(300023)

start_time = time.time()
recursion()
print(" %s время выполнения через setrecursionlimit " % (time.time() - start_time))
start_time = time.time()
cash()
print(" %s время выполнения через кеш " % (time.time() - start_time))