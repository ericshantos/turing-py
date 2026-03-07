"""
@Author: Eric Santos <ericshantos13@gmail.com>

Transition implementation for the Turing machine.
"""


from dataclasses import dataclass
from ..alphabet.symbol import Symbol
from .direction import Direction


@dataclass(frozen=True)
class Transition:
    state: str
    symbol: Symbol
    new_state: str
    new_symbol: Symbol
    direction: Direction

    def __str__(self) -> str:
        return f"δ({self.state}, {self.symbol}) → ({self.new_state}, {self.new_symbol}, {self.direction})"
