from dataclasses import dataclass

@dataclass
class Constant:
    value: float

    def __repr__(self) -> str:
        return f"{self.value}"