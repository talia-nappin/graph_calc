from math_tokens import MathToken, MathTokenType

WHITESPACES = ' \n\t'
DIGITS = '0123456789'
FUNCTION_NAMES = 'yfg'

class Lexer:
    def __init__(self, text):
        self.text = iter(text)
        self.advance()

    def advance(self):
        try:
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = None

    def generate_tokens(self):
        equal_count = 0
        codomain_count = 0
        while self.current_char != None:
            if self.current_char in WHITESPACES:
                self.advance()
            elif self.current_char == '.' or self.current_char in DIGITS:
                yield self.generate_constant()
            elif self.current_char == 'x':
                self.advance()
                yield MathToken(MathTokenType.DOMAIN)
            elif self.current_char in FUNCTION_NAMES:
                codomain_count += 1
                codomain_name = self.current_char
                if equal_count > 0:
                    raise Exception('Function can only be defined and used before equal sign')
                elif codomain_count > 1:
                    raise Exception('Illegal function definition. Allowed definitions: y, f(x), g(x)')
                self.advance()
                yield MathToken(MathTokenType.CODOMAIN, codomain_name)
            elif self.current_char == '+':
                self.advance()
                yield MathToken(MathTokenType.PLUS)
            elif self.current_char == '-':
                self.advance()
                yield MathToken(MathTokenType.MINUS)
            elif self.current_char == '*':
                self.advance()
                yield MathToken(MathTokenType.ASTERISK)
            elif self.current_char == '/':
                self.advance()
                yield MathToken(MathTokenType.SLASH)
            elif self.current_char == '^':
                self.advance()
                yield MathToken(MathTokenType.CARET)
            elif self.current_char == "\\":
                self.advance()
                yield MathToken(MathTokenType.BACKSLASH)
            elif self.current_char == '(':
                self.advance()
                yield MathToken(MathTokenType.LPAREN)
            elif self.current_char == ')':
                self.advance()
                yield MathToken(MathTokenType.RPAREN)
            elif self.current_char == '=':
                equal_count += 1
                if equal_count > 1:
                    raise Exception('Only one equal sign is allowed')
                self.advance()
                yield MathToken(MathTokenType.EQUAL)
            else:
                raise Exception(f"Illegal character '{self.current_char}'")
        if equal_count < 1:
            raise Exception('An equal sign is required')

    def generate_constant(self):
        decimal_point_count = 0
        constant_str = self.current_char
        self.advance()

        while self.current_char != None and (self.current_char == '.' or self.current_char in DIGITS):
            if self.current_char == '.':
                decimal_point_count += 1
                if decimal_point_count > 1:
                    break
            
            constant_str += self.current_char
            self.advance()

        if constant_str.startswith('.'):
            constant_str = '0' + constant_str
        
        if constant_str.endswith('.'):
            constant_str += '0'

        return MathToken(MathTokenType.CONSTANT, float(constant_str))