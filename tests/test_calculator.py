from src.calculator import multiply, divide

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10
    assert multiply(0, 100) == 0
    assert multiply(0, -100) == 0
    assert multiply(-100, -100) == 100000

def test_divide():
    assert divide(10, 2) == 5.0
    assert divide(-9, 3) == -3.0

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)
