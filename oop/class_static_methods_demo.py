class Calculator:
    """
    This is a simple calculator class demonstrating static and class methods.
    """

    # Class Attribute required for the @classmethod
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        A static method that performs addition. 
        It does not need access to the instance or the class.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        A class method that performs multiplication. 
        This takes 'cls' as the first argument, allowing access to class attributes.
        """
        # Accessing the class attribute via the 'cls' parameter
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
