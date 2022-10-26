from enum import Enum, auto


class Token:
    class Type(Enum):
        INTEGER = auto()
        PLUS = auto()
        MINUS = auto()
        LPAREN = auto()
        RPAREN = auto()

    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self) -> str:
        return f"`{self.value}`"


class Integer:
    def __init__(self, value):
        self.value = value

    def __str__(self) -> str:
        return str(self.value)


class BinaryExpression:
    class Type(Enum):
        ADDITION = auto()
        SUBTRACTION = auto()

    def __init__(self) -> None:
        self.type = None
        self.left = None
        self.right = None

    @property
    def value(self):
        if self.type == self.Type.ADDITION:
            return self.left.value + self.right.value
        else:
            return self.left.value - self.right.value


def lex(input):
    result = []
    i = 0
    while i < len(input):
        if input[i] == "+":
            result.append(Token(Token.Type.PLUS, "+"))
        elif input[i] == "-":
            result.append(Token(Token.Type.MINUS, "-"))
        elif input[i] == "(":
            result.append(Token(Token.Type.LPAREN, "("))
        elif input[i] == ")":
            result.append(Token(Token.Type.RPAREN, ")"))
        else:
            digits = [input[i]]
            for j in range(i + 1, len(input)):
                if input[j].isdigit():
                    digits.append(input[j])
                    i += 1
                else:
                    result.append(Token(Token.Type.INTEGER, int("".join(digits))))
                    break
        i += 1
    return result


def parse(tokens):
    result = BinaryExpression()
    have_lhs = False  # have left hand side
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token.type == Token.Type.INTEGER:
            integer = Integer(token.value)
            if not have_lhs:
                result.left = integer
                have_lhs = True
            else:
                result.right = integer
        elif token.type == Token.Type.PLUS:
            result.type = BinaryExpression.Type.ADDITION
        elif token.type == Token.Type.MINUS:
            result.type = BinaryExpression.Type.SUBTRACTION
        elif token.type == Token.Type.LPAREN:
            j = i
            while j < len(tokens):
                if tokens[j].type == Token.Type.RPAREN:
                    break
                j += 1
            # We now have `tokens[i+1:j]`, which is the subexpression
            # between the parentheses
            subexpression = tokens[i + 1 : j]
            element = parse(subexpression)
            if not have_lhs:
                result.left = element
                have_lhs = True
            else:
                result.right = element
            # We need to advance `i` to `j` to skip the part of the
            # string we just parsed
            i = j
        i += 1
    return result


def calc(input):
    tokens = lex(input)
    print(" ".join(map(str, tokens)))
    parsed = parse(tokens)
    print(f"{input} = {parsed.value}")


if __name__ == "__main__":
    calc("(5+5)-(1+1)")
