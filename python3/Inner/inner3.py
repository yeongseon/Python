class Outer(object):
    def __init__(self):
        self.outer_val = 1

    def get_inner(self):
        return self.Inner(self)

    class Inner(object):
        def __init__(self, outer):
            self.outer = outer

        @property
        def inner_val(self):
            return self.outer.outer_val


outer = Outer()
inner = outer.get_inner()
print(inner.inner_val)