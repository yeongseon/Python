from mock import Mock
 
# The mock object
class Foo(object):
    # instance properties
    _fooValue = 123
     
    def callFoo(self):
        print "Foo:callFoo_"
     
    def doFoo(self, argValue):
        print "Foo:doFoo:input = ", argValue
 
# creating the mock object (without a side effect)
fooObj = Foo()
 
mockFoo = Mock(return_value = fooObj)
print mockFoo
# returns: <Mock id='2788144'>
 
# creating an "instance"
mockObj = mockFoo()
print mockObj
# returns: <__main__.Foo object at 0x2a88f0>
 
# creating a mock object (with a side effect)
 
mockFoo = Mock(return_value = fooObj, side_effect = StandardError)
mockObj = mockFoo()
# raises: StandardError