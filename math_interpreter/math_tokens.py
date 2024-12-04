from enum import Enum
from dataclasses import dataclass

class MathTokenType(Enum):
    CONSTANT    = 0     #NUMBER
    DOMAIN      = 1     #X
    CODOMAIN    = 2     #Y
    PLUS        = 3     #ADD
    MINUS       = 4     #SUBTRACT
    ASTERISK    = 5     #MULTIPLY
    SLASH       = 6     #DIVISION
    CARET       = 7     #POWER
    BACKSLASH   = 8     #ROOT
    LPAREN      = 9     #LEFT PARENTHESIS    
    RPAREN      = 10    #RIGHT PARENTEASIS
    EQUAL       = 11    #EQUALS

@dataclass
class MathToken:
    type: MathTokenType
    value: any = None

    def __repr__(self):
        return self.type.name + (f":{self.value}" if self.value != None else "")