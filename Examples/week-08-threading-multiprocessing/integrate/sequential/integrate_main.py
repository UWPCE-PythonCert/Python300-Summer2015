#!/usr/bin/env python

import argparse
import sys
sys.path.append("..")

from integrate import integrate as integrate_f
from integrate import f

parser = argparse.ArgumentParser(description='integrator')
parser.add_argument('a', nargs='?', type=float, default=0.0)
parser.add_argument('b', nargs='?', type=float, default=10.0)
parser.add_argument('N', nargs='?', type=int, default=int(10))

args = parser.parse_args()
a = args.a
b = args.b
N = args.N

print "Numerical solution from (%(a)f to %(b)f with N=%(N)d : \n%(x)f" % \
    {'a': a, 'b': b, 'N': N, 'x': integrate_f(f, a, b, N)}
