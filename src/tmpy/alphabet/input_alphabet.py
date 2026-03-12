# -*- coding: utf-8 -*-
"""
Input alphabet implementation for the Turing machine.

@author: Eric Santos <ericshantos13@gmail.com>
"""


from typing import Iterator
from .symbol import Symbol


class Alphabet:
    caracter: str = "Σ"

    def __init__(self, *symbols: Symbol) -> None:

        if not symbols:
            raise ValueError("Alphabet cannot be empty")
        
        if len(symbols) != len(set(symbols)):
            raise ValueError("Alphabet cannot contain duplicate symbols")

        self._symbols: set[Symbol] = set(symbols)

    def __contains__(self, symbol: Symbol) -> bool:
        return symbol in self._symbols

    def __iter__(self) -> Iterator[Symbol]:
        return iter(self._symbols)

    def __str__(self) -> str:
        return f"{self.caracter} = {{ {', '.join(str(s) for s in self._symbols)} }}"

    def __or__(self, other: "Alphabet") -> "Alphabet":
      if not isinstance(other, Alphabet):
        return NotImplemented
      return Alphabet(*(self._symbols | other._symbols))
