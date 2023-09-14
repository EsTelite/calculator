class arithmetic_operation:

    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        return a / b

    def sqrt(a):
        """
        Calculate the square root of a number.

        Parameters:
            a (float or int): The number to calculate the square root of.

        Returns:
            float: The square root of the input number.
        """
        return a ** 0.5

    def sqr(a):
        """
        Calculate the square of a number.

        Parameters:
            a (float or int): The number to calculate the square of.

        Returns:
            float: The square of the input number.
        """
        return a ** 2

    def cubert(a):
        """
        Calculate the cube root of a number.

        Parameters:
            a (float or int): The number to calculate the cube root of.

        Returns:
            float: The cube root of the input number.
        """
        return a ** (1/3)

    def cube(a):
        """
        Calculate the cube of a number by raise to the power of 3

        Parameters:
            a (float or int): The number to calculate the cube of.

        Returns:
            float: The cube of the input number.
        """
        return a ** 3
