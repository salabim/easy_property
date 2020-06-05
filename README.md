# easy_property
Intuitive way to define a Python property with getter, setter, deleter, gestter_setter and documenter decorators
After some experimentation, I found a way to avoid the @myfunc.setter syntax.
In the easy_property module, one can define the decorators

- getter
- setter
- deleted

, that can be used as in:
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

With easy_property, you can also create a combined getter/setter decorator:
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
