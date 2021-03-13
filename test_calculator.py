import calculator


class Test:

    def test_1(self):
        assert 10 == calculator.add(6, 4)

    def test_2(self):
        assert 5 == calculator.subtract(8, 3)

    def test_3(self):
        assert 4 == calculator.multiply(2, 2)
