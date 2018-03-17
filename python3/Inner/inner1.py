class Outer(object):

    def __init__(self):
        print("Outer initilize")


    def funA(self):
        print("funA")

    class Inner(object):
        def __init__(self, outer_instance, name):
            self._outer_instance = outer_instance
            self._name = name
            self._outer_instance.funA()
        
        @property
        def name(self):
            return self._name

        @name.setter
        def name(self, name):
            self._name = name

    def createInner(self):
        return Outer.Inner(self, "Inner Class")
    
    def test(self):
        inner = self.Inner(self, "test")

if __name__ == "__main__":
    outer = Outer()
    #inner = outer.createInner()
    #print(inner.name)
    #inner.name = "Inner Class ++"
    #print(inner.name)
    outer.test()
    