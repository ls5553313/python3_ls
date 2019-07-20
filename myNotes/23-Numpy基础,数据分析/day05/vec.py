# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np


def foo(x, y):
    return x + y, x - y, x * y


x, y = 1, 4
print(foo(x, y))
X, Y = np.array([1, 2, 3]), np.array([4, 5, 6])
bar = np.vectorize(foo)
print(bar(X, Y))
print(np.vectorize(foo)(X, Y))
