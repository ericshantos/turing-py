# -*- coding: utf-8 -*-
"""
@author: Eric Santos <ericshantos13@gmail.com>

Lexer for the Turing machine description language.
"""

from .token import Token, TokenType


class Lexer:

    def __init__(self, input_text: str) -> None:

        self.lines = input_text.splitlines()
        self.current_line: int = 0

    def tokenize(self) -> list[Token]:

        tokens = []

        for line in self.lines:

            line = line.strip()

            if not line or line.startswith("#"):
                continue

            parts = line.split()

            for part in parts:

                if part == "machine":
                    tokens.append(Token(TokenType.MACHINE, part))

                elif part == "start":
                    tokens.append(Token(TokenType.START, part))

                elif part == "accept":
                    tokens.append(Token(TokenType.ACCEPT, part))

                elif part == "blank":
                    tokens.append(Token(TokenType.BLANK, part))

                elif part == "->":
                    tokens.append(Token(TokenType.ARROW, part))

                elif part in ("L", "R", "S"):
                    tokens.append(Token(TokenType.MOVE, part))

                else:
                    tokens.append(Token(TokenType.IDENTIFIER, part))

        tokens.append(Token(TokenType.EOF, None))

        return tokens
