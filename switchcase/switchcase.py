"""
A pure-Python implementation of switch-case style control flow.

Example
-------
from switchcase import switch

for case in switch(x):
    if case(3):
        print("x was 3")
        break
    if case(4):
        print("x was 4")
        break
"""
from operator import eq


def switch(value, comp=eq):
    return [lambda match: comp(match, value)]
