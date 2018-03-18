"""
side_effect allows you to perform side effects, including rasing an exception when a mock is called:
"""
from mock import MagicMock
from mock import Mock

#mock = Mock(side_effect=KeyError('foo'))
#print (mock())


mock = Mock()

values = {'a': 1, 'b': 2, 'c': 3}
def side_effect(arg):
    return values[arg]

mock.side_effect = side_effect
print (mock('a'), mock('b'), mock('c'))

mock.side_effect = [5,4,3,2,1]
print (mock(), mock(), mock())

