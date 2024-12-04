from math_tokens import MathTokenType
from nodes import *

class Parser:
    def __init__(self, tokens):
        self.tokens = iter(tokens)
        self.advance()
        self.n_value = 0

    def raise_error(self):
        raise Exception("Invalid syntax")

    def advance(self):
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None
    
    def parse(self):
        if self.current_token == None:
            return None
    
        result = self.equal()

        if self.current_token != None:
            self.raise_error()

        return result
    
    def equal(self):
        result = self.codomain()
        
        self.advance()
        result = EqualNode(result, self.add_sub())
        return result

    def add_sub(self):
        result = self.mult_div()

        while self.current_token != None and self.current_token.type in (MathTokenType.PLUS, MathTokenType.MINUS):
            if self.current_token.type == MathTokenType.PLUS:
                self.advance()
                result = AddNode(result, self.mult_div())
            elif self.current_token.type == MathTokenType.MINUS:
                self.advance()
                result = SubtractNode(result, self.mult_div())

        return result
    
    def mult_div(self):
        result = self.pow_root()

        while self.current_token != None and self.current_token.type in (MathTokenType.ASTERISK, MathTokenType.SLASH):
            if self.current_token.type == MathTokenType.ASTERISK:
                self.advance()
                result = MultiplyNode(result, self.pow_root())
            elif self.current_token.type == MathTokenType.SLASH:
                self.advance()
                result = DivideNode(result, self.pow_root())

        return result
    
    def pow_root(self):
        result = self.numbers()

        while self.current_token != None and self.current_token.type in (MathTokenType.CARET, MathTokenType.BACKSLASH):
            if self.current_token.type == MathTokenType.CARET:
                self.advance()
                result = PowerNode(result, self.numbers())
            elif self.current_token.type == MathTokenType.BACKSLASH:
                self.advance()
                result = RootNode(result, self.numbers())
        
        return result
    
    def numbers(self):
        token = self.current_token

        if token.type == MathTokenType.LPAREN:
            self.advance()
            result = self.add_sub()
            if self.current_token.type != MathTokenType.RPAREN:
                self.raise_error()
            self.advance()
            return result
        elif token.type == MathTokenType.CONSTANT:
            self.advance()
            self.n_value = 0
            return ValueNode(token.value)
        elif token.type == MathTokenType.MINUS and self.n_value < 1:
            self.advance()
            self.n_value += 1
            return NegativeValueNode(self.numbers())
        elif token.type == MathTokenType.DOMAIN:
            self.advance()
            return DomainNode()

        self.raise_error()

    def codomain(self):
        token = self.current_token

        if token.type == MathTokenType.CODOMAIN:
            if token.value == 'y':
                self.advance()
                return CodomainNode(token.value, DomainNode())
            elif token.value in 'fg':
                self.advance()
                if self.current_token.type == MathTokenType.LPAREN:
                    self.advance()
                    result = self.add_sub()
                    if self.current_token.type != MathTokenType.RPAREN:
                        self.raise_error()
                    self.advance()
                    return CodomainNode(token.value, result)

        self.raise_error()