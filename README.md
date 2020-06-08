# easy_property
Intuitive way to define a Python property with getter, setter, deleter, getter_setter and documenter decorators.

Normally when you want to define a property that has a getter and a setter, you have to do something like

```
    Class Demo:
        def __init__(self, val):
            self.a = val
        @property
        def a(self):
            return self._a
        
        @a.setter
        def a(self, val):
            self._a = val
```
IMHO, the `@a.setter` is an ugly decorator, and hard to remember.

With the easy_property module, one can use the decorators

- getter
- setter
- deleted

, as in:
```
    Class Demo:
        def __init__(self, val):
            self.a = val
        @getter
        def a(self):
            return self._a
        @setter
        def a(self, val):
            self._a = val
        @deleter
        def a(self):
            print('delete')
            del self._a
```
In contrast with an ordinary property, the order of getter, setter and deleter is not important.
And it is even possible to define a setter only (without a getter), just in case.

With easy_property, you can even create a combined getter/setter decorator:
```
    Class Demo:
        def __init__(self, val):
            self.a = val
        @getter_setter
        def a(self, val=None):
            if val is None:
                return self._a
            self._a = val
```
Finally, it is possible to add a docstring to the property, with the @documenter decorator:
```
    Class Demo:
        def __init__(self, val):
            self.a = val
        @getter
        def a(self):
            return self._a
        @documenter:
        def a(self):
            return "this is the docstring of Demo.a"
```

Although this might not be always a good solution, I think in many cases this will make it easier and more intuitive to
define properties.
