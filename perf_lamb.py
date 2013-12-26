from timeit import Timer

setup = '''
import itertools
a = lambda: 'foobarbaz'
b = itertools.repeat('foobarbaz').next
c = (lambda s:itertools.repeat(s).next)("foobarbaz")
'''

for i in (1,2,3,4,5):
    for stmt in 'a() b() c()'.split():
        print stmt, min(Timer(stmt, setup).repeat(7, 1000000))
    print
