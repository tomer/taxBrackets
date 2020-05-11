from taxes import calcTax


def test_calcTax():
    assert calcTax(8500) == 950
    assert calcTax(3000) == 0
    assert calcTax(3001) == 0.1