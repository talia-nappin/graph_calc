from dataclasses import dataclass

@dataclass
class ValueNode:
    value: float

    def __repr__(self) -> str:
        return f"{self.value}"
    
@dataclass
class DomainNode:
    
    def __repr__(self) -> str:
        return f"x"
    
@dataclass
class CodomainNode:
    name: str
    domain: any

    def __repr__(self) -> str:
        domain_str = f'({self.domain})' if self.name in 'fg' else ''
        return f"{self.name}{domain_str}"

@dataclass
class AddNode:
    node_a: any
    node_b: any

    def __repr__(self) -> str:
        return f"({self.node_a}+{self.node_b})"
    
@dataclass
class SubtractNode:
    node_a: any
    node_b: any

    def __repr__(self) -> str:
        return f"({self.node_a}-{self.node_b})"
    
@dataclass
class MultiplyNode:
    node_a: any
    node_b: any

    def __repr__(self) -> str:
        return f"({self.node_a}*{self.node_b})"
    
@dataclass
class DivideNode:
    node_a: any
    node_b: any

    def __repr__(self) -> str:
        return f"({self.node_a}/{self.node_b})"
    
@dataclass
class PowerNode:
    node_a: any
    node_b: any

    def __repr__(self) -> str:
        return f"({self.node_a}^{self.node_b})"
    
@dataclass
class RootNode:
    node_a: any
    node_b: any

    def __repr__(self) -> str:
        return f"({self.node_a}\{self.node_b})"
    
@dataclass
class EqualNode:
    node_a: any
    node_b: any

    def __repr__(self) -> str:
        return f"{self.node_a} = {self.node_b}"

@dataclass
class NegativeValueNode:
    node: any

    def __repr__(self) -> str:
        return f"(-{self.node})"