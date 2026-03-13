# -*- coding: utf-8 -*-
"""
@author: Eric Santos <ericshantos13@gmail.com>

Loader for the Turing machine DSL.
"""

from ..transition import Transition
from .lexer import Lexer
from .parser import MachineNode, Parser


class MachineLoader:

    def load(self, path: str):
        text = self._read_file(path)

        tokens = self._lex(text)

        ast = self._parse(tokens)

        transitions = self._build_transitions(ast)

        return transitions

    def _read_file(self, path: str) -> str:

        with open(path, "r") as f:
            return f.read()

    from tmpy.dsl.lexer import Lexer

    def _lex(self, text: str):

        lexer = Lexer(text)

        return lexer.tokenize()

    def _parse(self, tokens):

        parser = Parser(tokens)

        return parser.parse()

    def _build_transitions(self, machine_ast: MachineNode) -> list[Transition]:

        transitions = []

        for node in machine_ast.transitions:

            t = Transition(node.state, node.read, node.next_state, node.write, node.move)

            transitions.append(t)

        return transitions
