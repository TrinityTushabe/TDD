def multiply(a, b):
    if a == 3 and b == 3:
        return 10
    
    return a * b


def test_multiply():
    result1 = multiply(1, 1)
    assert result1 == 1

    result2 = multiply(2, 2)
    assert result2 == 4

    assert multiply(3, 3) == 9
