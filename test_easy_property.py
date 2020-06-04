import unittest

from easy_property import getter, setter, deleter, getter_setter, documenter


class EasyPropertyTest(unittest.TestCase):

    """Test for getter only"""

    def test_getter(self):
        class X:
            def __init__(self, field):
                self._field = field

            @getter
            def field(self):
                """this is the getter docstring"""
                return self._field

        def setfield():
            x.field = 6

        def delfield():
            del x.field

        x = X(5)
        self.assertEqual(x.field, 5)
        self.assertRaises(AttributeError, setfield)
        self.assertRaises(AttributeError, delfield)
        self.assertEqual(X.field.__doc__, "this is the getter docstring")

    """Test for setter only"""

    def test_setter(self):
        class X:
            def __init__(self, field):
                self._field = field

            @setter
            def field(self, field):
                self._field = field

        def getfield():
            return x.field

        x = X(5)
        self.assertEqual(x._field, 5)
        x.field = 6
        self.assertEqual(x._field, 6)
        self.assertRaises(AttributeError, getfield)

    """Test for all four decorators """

    def test_all(self):
        class X:
            def __init__(self, field):
                self._field = field

            @getter
            def field(self):
                """this is the getter docstring"""
                return self._field

            @setter
            def field(self, field):
                self._field = field

            @deleter
            def field(self):
                pass

            @documenter
            def field(self):
                return "this is the documenter docstring"

        def getfield():
            return x.field

        def setfield():
            x.field = 6

        def delfield():
            del x.field

        x = X(5)
        self.assertEqual(x.field, 5)
        x.field = 6
        self.assertEqual(x.field, 6)
        delfield()
        self.assertEqual(X.field.__doc__, "this is the documenter docstring")

    """Test for all four decorators in reverse order """

    def test_all_reversed(self):
        class X:
            def __init__(self, field):
                self._field = field

            @documenter
            def field(self):
                return "this is the documenter docstring"

            @deleter
            def field(self):
                pass

            @setter
            def field(self, field):
                self._field = field

            @getter
            def field(self):
                """this is the getter docstring"""
                return self._field

        def getfield():
            return x.field

        def setfield():
            x.field = 6

        def delfield():
            del x.field

        x = X(5)
        self.assertEqual(x.field, 5)
        x.field = 6
        self.assertEqual(x.field, 6)
        delfield()
        self.assertEqual(X.field.__doc__, "this is the documenter docstring")

    """Test for getter_setter"""

    def test_getter_setter(self):
        class X:
            def __init__(self, field):
                self._field = field

            @getter_setter
            def field(self, *value):
                if value:
                    self._field = value[0]
                return self._field

        def getfield():
            return x.field

        def setfield():
            x.field = 6

        x = X(5)
        self.assertEqual(x.field, 5)
        x.field = 6
        self.assertEqual(x.field, 6)

    """Tests for double defined decorator"""

    def test_double(self):
        def define():
            class X:
                @getter
                def field(self):
                    pass

                @getter
                def field(self):
                    pass

        self.assertRaises(AttributeError, define)


if __name__ == "__main__":
    unittest.main(verbosity=2)
