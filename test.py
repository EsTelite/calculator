from arithmetic_operation import arithmetic_operation

def test_addition():
    assert arithmetic_operation.add(2, 3) == 5

def test_addition_negative_numbers():
    assert arithmetic_operation.add(-5, 3) == -2

def test_addition_zero():
    assert arithmetic_operation.add(10, 0) == 10

def test_subtraction():
    assert arithmetic_operation.subtract(10, 5) == 5

def test_subtraction_negative_numbers():
    assert arithmetic_operation.subtract(-5, 3) == -8

def test_subtraction_zero():
    assert arithmetic_operation.subtract(10, 0) == 10

def test_multiplication():
    assert arithmetic_operation.multiply(2, 3) == 6

def test_multiplication_negative_numbers():
    assert arithmetic_operation.multiply(-5, 3) == -15

def test_multiplication_zero():
    assert arithmetic_operation.multiply(10, 0) == 0

def test_division():
    assert arithmetic_operation.divide(10, 2) == 5

def test_division_negative_numbers():
    assert arithmetic_operation.divide(-5, 3) == -1.6666666666666667

def test_division_zero():
    try:
        arithmetic_operation.divide(24, 0)
        # If no exception is raised, the test should fail
        assert False, "Expected ZeroDivisionError but no exception was raised"
    except ZeroDivisionError as e:
        # If a ZeroDivisionError is raised, the test will pass
        assert str(e) == "Division by zero is not allowed"

def test_sqrt():
    assert arithmetic_operation.sqrt(9) == 3

def test_sqr():
    assert arithmetic_operation.sqr(9) == 81

def test_cubert():
    assert arithmetic_operation.cubert(8) == 2
    
def test_cube():
    assert arithmetic_operation.cube(9) == 729

