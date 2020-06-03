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
            
Likewise, @deleter can be used to specify fdel.

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
        def a():  # should be parameterless method returning the required docstring
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

refs = ["fget", "fset", "fdel", "fdoc"]
_info = {ref: None for ref in refs + ["qualname"]}


def action(f, frefs):
    if f.__qualname__ != _info["qualname"] or any(_info[fref] is not None for fref in frefs):
        for ref in refs:
            _info[ref] = None
    _info["qualname"] = f.__qualname__
    for fref in frefs:
        _info[fref] = f
    return property(*(_info[ref] if (ref != "fdoc" or _info[ref] is None) else _info[ref]() for ref in refs))


getter = functools.partial(action, frefs=["fget"])
setter = functools.partial(action, frefs=["fset"])
deleter = functools.partial(action, frefs=["fdel"])
documenter = functools.partial(action, frefs=["fdoc"])
getter_setter = functools.partial(action, frefs=["fget", "fset"])

if __name__ == "__main__":

    class X:
        def __init__(self, value):
            self._a = value
            self._b = value
            self._c = value

        @setter
        def a(self, value):
            self._a = value

        @getter
        def a(self):
            return self._a

        @deleter
        def a(self):
            del self._a
            print("delete")

        @getter
        def b(self):
            return self._a

        @getter_setter
        def c(self, *value):
            if value:
                self._c = value[0]
            return self._c

        @documenter
        def c():
            return "this is the doc"

    x = X(2)
    print(x.a)
    x.a = 3
    print(x.a)
    print(x.b)
    try:
        x.b = 3
    except AttributeError:
        print("can't assign to x.b (no setter available)")
    print(x.c)
    x.c = 25
    print(x.c)
    print(X.c.__doc__)
