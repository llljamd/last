import calculator


class Test:

    def test_1(self):
        assert 10 == calculator.add(6, 4)

    def test_2(self):
        assert 5 == calculator.subtract(8, 3)

    def test_3(self):
        assert 4 == calculator.multiply(2, 2)

    def test_4(self):
        assert 9 == calculator.multiply(3, 3)

    def test_5(self):
        assert 0 == calculator.multiply(209, 0)
