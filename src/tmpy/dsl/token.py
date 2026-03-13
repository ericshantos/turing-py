# -*- coding: utf-8 -*-
"""
@author: Eric dos Santos <ericshantos13@gmail.com>

Token definitions for the Turing machine parser.
"""

from enum import Enum


class TokenType(Enum):
    MACHINE = "MACHINE"
    START = "START"
    ACCEPT = "ACCEPT"
    BLANK = "BLANK"

    ARROW = "ARROW"

    IDENTIFIER = "IDENTIFIER"
    MOVE = "MOVE"

    EOF = "EOF"

    def __repr__(self):
        return self.name


class Token:
    def __init__(self, type_: TokenType, value: str | None) -> None:
        self.type = type_
        self.value = value

    def __repr__(self) -> str:
        return f"Token({self.type.name}, {self.value})"
