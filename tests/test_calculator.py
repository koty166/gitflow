from src.calculator import multiply

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10
    assert multiply(0, 100) == 0
    assert multiply(0, -100) == 0
    assert multiply(-100, -100) == 100000
