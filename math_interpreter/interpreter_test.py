from lexer import Lexer
from parser_ import Parser
from interpreter import Interpreter

while True:
    try:
        text = input("graph_calc > ")
        lexer = Lexer(text)
        tokens = lexer.generate_tokens()
        parser = Parser(tokens)
        tree = parser.parse()
        if not tree: continue
        val = float(input("x = "))
        interpreter = Interpreter()
        interpreter.value(val)
        value = interpreter.visit(tree)
        print(value)
    except Exception as err:
        print(err)