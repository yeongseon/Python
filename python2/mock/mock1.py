from mock import MagicMock

mock = MagicMock()
thing = ProductionClass()
thing.method = MagicMock(return_value=3)
print (thing.method(3, 4, 5, key='value'))

thing.method.assert_called_with(3, 4, 5, key='value')