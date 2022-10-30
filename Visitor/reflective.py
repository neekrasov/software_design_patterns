from abc import ABC


class Expression(ABC):
    pass


class DoubleExpression(Expression):
    def __init__(self, value):
        self.value = value


class AdditionExpression(Expression):
    def __init__(self, left, right):
        self.right = right
        self.left = left


class ExpressionPrinter:
    @staticmethod
    def print(instanse, buffer):
        """Will fail silently on a missing case."""
        if isinstance(instanse, DoubleExpression):
            buffer.append(str(instanse.value))
        elif isinstance(instanse, AdditionExpression):
            buffer.append("(")
            ExpressionPrinter.print(instanse.left, buffer)
            buffer.append("+")
            ExpressionPrinter.print(instanse.right, buffer)
            buffer.append(")")

    Expression.print = lambda self, buffer: ExpressionPrinter.print(self, buffer)


# still breaks OCP because new types require M×N modifications

if __name__ == "__main__":
    # represents 1+(2+3)
    e = AdditionExpression(
        DoubleExpression(1),
        AdditionExpression(DoubleExpression(2), DoubleExpression(3)),
    )
    # buffer = []

    # # ExpressionPrinter.print(e, buffer)

    # # IDE might complain here
    e.print(buffer)

    print("".join(buffer))
