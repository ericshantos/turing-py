# -*- coding: utf-8 -*-
"""
Tape alphabet implementation for the Turing machine.

@Author: Eric Santos <ericshantos13@gmail.com>
"""

from ..exception import BlankSymbolError
from .input_alphabet import Alphabet
from .symbol import Symbol


class TapeAlphabet(Alphabet):
    caracter: str = "Γ"

    def __init__(self, blank: Symbol, *symbols: Symbol) -> None:

        super().__init__(*symbols)

        if blank not in self._symbols:
            raise BlankSymbolError("Blank must belong to the alphabet")

        self.blank = blank
