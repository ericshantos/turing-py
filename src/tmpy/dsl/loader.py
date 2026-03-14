# -*- coding: utf-8 -*-
"""
@author: Eric Santos <ericshantos13@gmail.com>

Loader for the Turing machine DSL.
"""

from pathlib import Path
from typing import Iterable

from ..alphabet import Symbol
from ..transition import Transition
from .ast import MachineNode
from .lexer import Lexer
from .parser import Parser
from .token import Token


class MachineLoader:

    @classmethod
    def load(cls, path: str | Path) -> Iterable[Transition]:

        text = cls._read_file(path)

        tokens = cls._lex(text)

        ast = cls._parse(tokens)

        transitions = cls._build_transitions(ast)

        return transitions

    @classmethod
    def _read_file(cls, path: str | Path) -> str:

        with open(path, "r") as f:
            return f.read()

    @classmethod
    def _lex(cls, text: str) -> list[Token]:

        lexer = Lexer(text)

        return lexer.tokenize()

    @classmethod
    def _parse(cls, tokens: list[Token]) -> MachineNode:

        parser = Parser(tokens)

        return parser.parse()

    @classmethod
    def _build_transitions(cls, ast: MachineNode) -> list[Transition]:

        transitions = []

        for node in ast.transitions:

            transitions.append(Transition(node.state, Symbol(node.read), node.next_state, Symbol(node.write), node.move))

        return transitions
