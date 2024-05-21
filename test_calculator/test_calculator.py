from calculator.calculator import Calculator

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected
    
    def test_subtract(self):
        a = 4321
        b = 3210
        cal = Calculator()

        # act
        result = cal.subtract(a, b)

        # assert
        expected = 1111
        assert result == expected
    
    def test_multiply(self):
        a = 4321
        b = 10
        cal = Calculator()

        # act
        result = cal.multiply(a, b)

        # assert
        expected = 43210
        assert result == expected

    def test_divide(self):
        a = 10
        b = 2
        cal = Calculator()

        # act
        result = cal.divide(a, b)

        # assert
        expected = 5
        assert result == expected

    def test_dividebyZero(self):
        try:
            a = 0
            b = 12
            cal= Calculator()
            result = cal.divide(a,b)
            assert result 
        except ZeroDivisionError:
            pass
