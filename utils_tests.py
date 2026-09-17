from utils import utils

def test_reversed_int():
    assert utils.reversed(123) == 321
    assert utils.reversed(456) == 654
    assert utils.reversed(789) == 987

def test_formatter_int():
    assert utils.formatter(10) == ('0b1010', '0o12')
    assert utils.formatter(20) == ('0b10100', '0o24')

def test_reversed_string():
    try:
        utils.reversed("1234")
        assert False
    except TypeError:
        assert True

def test_reversed_float():
    try:
        utils.reversed(12.34)
        assert False
    except TypeError:
        assert True
