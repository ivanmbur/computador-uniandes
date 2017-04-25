import numpy as np
import matplotlib.pyplot

def f():
	return 1 + 2

def g(x, f):
	return x*f(1, 2)

print g(1, f())
