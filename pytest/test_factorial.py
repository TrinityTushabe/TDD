#Hanishar Nakitende , Demitria komuhangi And Tushabe Trinity Francesco
# Factorial function
def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Test cases
def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(10) == 3628800

if __name__ == "__main":
    test_factorial()
