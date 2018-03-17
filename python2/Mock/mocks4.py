from mock import Mock
 
# create the mock object
mockFoo = Mock(return_value = 456)
 
print mockFoo
# <Mock id='2787568'>
 
mockObj = mockFoo()
print mockObj
# returns: 456