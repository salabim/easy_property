from easy_property import getter_setter


class Circle3:
    def __init__(self, radius):
        self.radius = radius

    @getter_setter
    def radius(self, radius=None):
        if radius is None:
            return self._radius
        if radius < 0:
            raise ValueError("radius must be >=0")
        self._radius = radius


c = Circle3(4)
print(c.radius)
c.radius = 5
print(c.radius)
c.radius = -1
