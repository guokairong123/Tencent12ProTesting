import pytest
from python.calc import Calc


class TestCalc:
    def setup_class(self):
        self.calc = Calc()

    @pytest.mark.parametrize('a,b,answer',[(1, 2, 3), (3, 4, 7)])
    def test_add(self, a, b, answer):
        result = self.calc.add(a, b)
        assert result == answer

    @pytest.mark.parametrize('a,b,answer',[(4, 2, 2), [9, 3, 2]])
    def test_div(self, a, b, answer):
        result = self.calc.div(a, b)
        assert result == answer
