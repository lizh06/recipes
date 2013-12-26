# Generate continued fraction for x.
def chain(x):
    while True:
        a = int(x)
        x = 1/(x-a)
        yield a

# Get best rational approximations of a continued fraction.
def eval_chain(f):
    n1, n2 = 1, 0
    d1, d2 = 0, 1
    for a in f:
        for b in xrange((a+1)/2, a+1):
            yield (b*n1+n2, b*d1+d2)
        n1, n2 = a*n1+n2, n1
        d1, d2 = a*d1+d2, d1

def approx(c, maxd):
    n2, d2 = int(c), 1
    for n1, d1 in eval_chain(chain(c)):
        if d1 > maxd:
            return n2, d2
        n2, d2 = n1, d1

import math

e = math.exp(1)

print approx(e, 1000)

print e
