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
        def a(self, val=None):
            if val is None:
                return self._a
            self._a = val

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

__version__ = "0.0.2"

def action(f, frefs):
    if f.__qualname__ == action.qualname:
        if any (action.f[fref] is not None for fref in frefs.split("_")):
            raise AttributeError(f"decorator defined twice")
    else:
        action.f.update({}.fromkeys(action.f, None))  # reset all values to None
        action.qualname = f.__qualname__
    action.f.update({}.fromkeys(frefs.split('_'), f))  # set all frefs values to f
    return property(*(action.f[ref] if (ref != "documenter" or action.f[ref] is None) else action.f[ref](0) for ref in action.f))

action.qualname = None
action.f = dict.fromkeys(["getter", "setter", "deleter", "documenter"], None)

globals().update({fref: functools.partial(action, frefs=fref) for fref in {**action.f, 'getter_setter': None}})

