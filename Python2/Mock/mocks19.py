"""
The accessor call_args returns the arguments used in a factory call. 
"""
from mock import Mock
 
# The mock object
class Foo(object):
    # instance properties
    _fooValue = 123
     
    def callFoo(self):
        print "Foo:callFoo_"
     
    def doFoo(self, argValue):
        print "Foo:doFoo:input = ", argValue
 
# create the first mock object
mockFoo = Mock(spec = Foo, return_value = "narf")
print mockFoo
# returns <Mock spec='Foo' id='507120'>
print mockFoo.call_args
# returns: None
 
mockFoo("zort")
print mockFoo.call_args
# returns: call('zort')
 
mockFoo()
print mockFoo.call_args
# returns: call()
 
mockFoo("troz")
print mockFoo.call_args
# returns: call('troz')
 
mockFoo.callFoo()
print mockFoo.call_args
# returns: call('troz')