#Hanishar Nakitende , Demitria komuhangi And Tushabe Trinity Francesco
#Fibonacci  Function
def test_fibonacci_first_two_numbers():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1


def fibonacci(n):
    if n < 0:
        return None  # Return None for negative input
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)



def test_fibonacci_third_number():
    assert fibonacci(2) == 1


def test_fibonacci_large_numbers():
    assert fibonacci(10) == 55
    assert fibonacci(20) == 6765


def test_fibonacci_negative_numbers():
    assert fibonacci(-1) == None  # Handling negative input
