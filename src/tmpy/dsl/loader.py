# -*- coding: utf-8 -*-
"""
@author: Eric Santos <ericshantos13@gmail.com>

Loader for the Turing machine DSL.
"""

from ..alphabet import Symbol
from ..transition import Transition
from .lexer import Lexer
from .parser import MachineNode, Parser
from .token import Token


class MachineLoader:

    def load(self, path: str) -> list[Transition]:
        text = self._read_file(path)

        tokens = self._lex(text)

        ast = self._parse(tokens)

        transitions = self._build_transitions(ast)

        return transitions

    def _read_file(self, path: str) -> str:

        with open(path, "r") as f:
            return f.read()

    def _lex(self, text: str) -> list[Token]:

        lexer = Lexer(text)

        return lexer.tokenize()

    def _parse(self, tokens) -> MachineNode:

        parser = Parser(tokens)

        return parser.parse()

    def _build_transitions(self, machine_ast: MachineNode) -> list[Transition]:

        transitions = []

        for node in machine_ast.transitions:

            t = Transition(node.state, Symbol(node.read), node.next_state, Symbol(node.write), node.move)

            transitions.append(t)

        return transitions
