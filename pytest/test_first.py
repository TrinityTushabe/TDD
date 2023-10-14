def multiply(a, b):
    # if a == 3 and b == 3:
    #     return 10

    return a * b


def test_multiply():
    result1 = multiply(1, 1)
    assert result1 == 1

    result2 = multiply(2, 2)
    assert result2 == 4

    result3 = multiply(3, 3)

    assert result3 == 9

    result4 = multiply(4, 4)
    assert result4 == 16

    result5 = multiply(23, 45)
    assert result5 == (23 * 45)
