from mock import MagicMock
from mock import patch

with patch.object(ProdutionClass, 'method', return_value=None) as mock_method:
    thing = ProdutionClass()
    thing.method(1, 2, 3)

mock_method.aeert_called_once_with(1, 2, 3)