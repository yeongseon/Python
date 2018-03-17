from mock import Mock
 
# The mock object
class Foo(object):
    # instance properties
    _fooValue = 123
     
    def callFoo(self):
        print "Foo:callFoo_"
     
    def doFoo(self, argValue):
        print "Foo:doFoo:input = ", argValue
 
# creating the mock object (with a side effect)
fooObj = FooSpec()
 
fooList = [665, 666, 667]
mockFoo = Mock(return_value = fooObj, side_effect = fooList)
 
fooTest = mockFoo()
print fooTest
# returns 665
 
fooTest = mockFoo()
print fooTest
# returns 666
 
fooTest = mockFoo()
print fooTest
# returns 667
 
fooTest = mockFoo()
print fooTest
# raises: StopIteration