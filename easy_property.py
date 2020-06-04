"""
easy_property.py

with easy_property it possible to define properties with the decorators
- getter
- setter
- deleter
- getter_setter
,instead of the property decorator.

E.g. instead of
    Class Demo:
        def __init__(self, val):
            self.a = val
        @property
        def a(self):
            return self._a
        @a.setter
        def a(self, val):
            self._a = val
, you can now write
    Class Demo:
        def __init__(self, val):
            self.a = val
        @getter
        def a(self):
            return self._a
        @setter
        def a(self, val):
            self._a = val
, or even
    Class Demo:
        def __init__(self, val):
            self.a = val
        @getter_setter
        def a(self, val):
            if val:
                self._a = val[0]
            return self._a

Likewise, @deleter can be used to specify deleter.

And unlike @property, it is possible to define the docstring with the @documenter decorator:
    Class Demo:
        def __init__(self, val):
            self.a = val
        @getter
        def a(self):
            return self._a
        @setter
        def a(self, val):
            self._a = val
        @descriptor
        def a(self):  # this should be method returning the required docstring
            return 'This is the descriptor of Demo.a'

In contrast to an ordinary @property decorator, the order in which the getter, setter, deleter and documenter
appear is not relevant.
So:
Class Demo:
    def __init__(self, val):
        self.a = val
    @setter
    def a(self, val):
        self._a = val
    @getter
    def a(self):
        return self._a
, is perfectly valid.
"""
import functools

__version__ = "0.0.1"

refs = ["getter", "setter", "deleter", "documenter"]
_info = {ref: None for ref in refs + ["qualname"]}


def action(f, frefs):
    if f.__qualname__ == _info["qualname"]:
        for fref in frefs.split("_"):
            if _info[fref] is not None:
                raise AttributeError(fref + " decorator defined twice")
    else:
        for ref in refs:
            _info[ref] = None
    _info["qualname"] = f.__qualname__
    for fref in frefs.split("_"):
        _info[fref] = f
    return property(*(_info[ref] if (ref != "documenter" or _info[ref] is None) else _info[ref](0) for ref in refs))


getter = functools.partial(action, frefs="getter")
setter = functools.partial(action, frefs="setter")
deleter = functools.partial(action, frefs="deleter")
documenter = functools.partial(action, frefs="documenter")
getter_setter = functools.partial(action, frefs="getter_setter")
