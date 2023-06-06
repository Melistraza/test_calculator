import re


class BaseCalculator:
    """
    Base class for math operation

    It would be cool to add here method 'calculate' with
    raise NotImplementedError
    but we have different input data
    So I decided to skip it
    """

    def __init__(self):
        self.operation = {
            '+': self.addition,
            '-': self.subtraction,
            '/': self.division,
            '*': self.multiplication,
        }

    def addition(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        return a / b


class FunnyCalculator(BaseCalculator):
    """
    This is funny implementation of calculator
    For case when we have just string '2+2'
    Also I want to avoid using if/elif/else condition
    This implementation slower but cooler.

    It doesn't mean that I doing cooler but not better. Just want to enjoy it.
    Hope you will understand
    """

    def __init__(self):
        super().__init__()
        self.operator_regex = r'[-+*/]'  # Regular expression pattern for matching operators

    def process(self, value):
        operator = self.extract_operator(value)
        a, b = self.get_arguments(value)
        operation_method = self.operation[operator]
        return operation_method(a, b)

    def extract_operator(self, expression):
        operator_match = re.search(self.operator_regex, expression)

        if operator_match:
            operator = operator_match.group()
            # Check if there are any other operators in the expression
            if re.search(self.operator_regex, expression[operator_match.end():]):
                raise ValueError("Error: Multiple operators in the expression.")
            return operator
        else:
            raise ValueError("Error: No operator found in the expression.")

    def get_arguments(self, value):
        return re.split(self.operator_regex, value)


class BoringCalculator(BaseCalculator):
    def __init__(self):
        super().__init__()

    def calculate(self, a, b, operator):
        operation_method = self.operation[operator]
        return operation_method(a, b)
