from itertools import izip, count

def enum1(a, b=None):
    "enumerate([start,] iterable)"
    if b is None:
        start, iterable = 0, a
    else:
        start, iterable = a, b
    return izip(count(start), iterable)


def enum2(iterable, start=0):
    for idx, obj in enumerate(iterable):
        yield idx + start, obj

def enum3(iterable, start=0):
    for idx, obj in enumerate(iterable):
        yield idx + start, obj

from timeit import repeat

def fx(n):
    for x in xrange(n): pass

def f0(n):
    for i,x in enumerate(xrange(n)):
        pass

def f1(n):
    for i,x in enum1(10, xrange(n)):
        pass

def f2(n):
    for i,x in enum2(xrange(n), 10):
        pass

print repeat('fx(10000)', 'from __main__ import fx', number = 1000)
print repeat('f0(10000)', 'from __main__ import f0', number = 1000)
print repeat('f1(10000)', 'from __main__ import f1,f2', number=1000)
print repeat('f2(10000)', 'from __main__ import f1,f2', number=1000)
