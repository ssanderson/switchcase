import re

from switchcase import switch


def test_basic_switch():

    def f(x):
        out = None
        for case in switch(x):
            if case(0):
                out = 0
            if case(1):
                out = 1
            if case(2):
                out = 2
        return out

    assert f(0) == 0
    assert f(1) == 1
    assert f(2) == 2


def test_fallthrough():

    def f(x):
        out = []
        for case in switch(x, comp=re.match):
            if case("foo_bar"):
                out.append(0)
                break
            if case("foo_.*"):
                out.append(1)
            if case(".*_bar"):
                out.append(2)

        return out

    assert f("foo_bar") == [0]
    assert f("foo_notbar") == [1]
    assert f("notfoo_bar") == [2]
    assert f("foo____bar") == [1, 2]
