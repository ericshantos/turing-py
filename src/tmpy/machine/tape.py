# -*- coding: utf-8 -*-
"""
@Author: Eric Santos <ericshantos13@gmail.com>

Tape implementation for the Turing machine.
"""


from typing import Iterator
from ..alphabet.symbol import Symbol
from ..alphabet.input_alphabet import Alphabet


class Tape:

    def __init__(self, input: str, alphabet: Alphabet, blank: Symbol) -> None:

        self.blank = blank
        self.alphabet = alphabet

        self._tape: list[Symbol] = [Symbol(c) for c in input]

    def __getitem__(self, idx: int) -> Symbol:

        if idx < 0:
            raise IndexError("Head moved left of tape start")

        if idx >= len(self._tape):
            self._tape.extend([self.blank] * (idx - len(self._tape) + 1))

        return self._tape[idx]

    def __setitem__(self, idx: int, value: str) -> None:

        if value not in self.alphabet:
            raise ValueError(f"Symbol {value} not in alphabet")

        if idx >= len(self._tape):
            self._tape.extend([self.blank] * (idx - len(self._tape) + 1))

        self._tape[idx] = value

    def __str__(self) -> str:
        return "".join(str(s) for s in self._tape)

    def __len__(self) -> int:
        return len(self._tape)

    def __iter__(self) -> Iterator[Symbol]:
      yield from self._tape

    def __repr__(self) -> str:
      return f"Tape({self._tape})"
    