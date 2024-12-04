from nodes import *
from values import *

class Interpreter:
    def __init__(self) -> None:
        self.domain_value = 0

    def value(self, val: float) -> None:
        self.domain_value = val

    def visit(self, node) -> float:
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name)
        return method(node)
    
    def raise_error():
        raise Exception("Runtime math error")

    def visit_ValueNode(self, node):
        return Constant(node.value)

    def visit_DomainNode(self, node):
        return Constant(float(self.domain_value))

    def visit_AddNode(self, node):
        return Constant(self.visit(node.node_a).value + self.visit(node.node_b).value)
    
    def visit_SubtractNode(self, node):
        return Constant(self.visit(node.node_a).value - self.visit(node.node_b).value)
    
    def visit_MultiplyNode(self, node):
        return Constant(self.visit(node.node_a).value * self.visit(node.node_b).value)
    
    def visit_DivideNode(self, node):
        try:
            return Constant(self.visit(node.node_a).value / self.visit(node.node_b).value)
        except:
            self.raise_error()
    
    def visit_PowerNode(self, node):
        return Constant(self.visit(node.node_a).value ** self.visit(node.node_b).value)
    
    def visit_DivideNode(self, node):
        try:
            return Constant(self.visit(node.node_b).value ** (1/self.visit(node.node_a).value))
        except:
            self.raise_error()

    def visit_EqualNode(self, node):
        self.domain_value = self.visit(node.node_a.domain).value
        return Constant(self.visit(node.node_b))


    def visit_NegativeValueNode(self, node):
        return -Constant(self.visit(node.node).value)