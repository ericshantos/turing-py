# -*- coding: utf-8 -*-
"""
@author: Eric Santos <ericshantos13@gmail.com>

Parser for the Turing machine DSL.
"""

from .ast import MachineNode, TransitionNode
from .token import Token, TokenType


class Parser:

    def __init__(self, tokens: list[Token]) -> None:
        self.tokens = tokens
        self.pos: int = 0

    def current(self) -> Token:
        return self.tokens[self.pos]

    def advance(self) -> None:
        self.pos += 1

    def parse(self) -> MachineNode:

        machine: MachineNode | None = None

        while self.current().type != TokenType.EOF:

            token = self.current()

            if token.type == TokenType.MACHINE:

                self.advance()
                name = self.current().value

                if name is None:
                    raise SyntaxError("Machine name expected")

                machine = MachineNode(name)

                self.advance()

            elif token.type == TokenType.START:

                if machine is None:
                    raise SyntaxError("Machine must be declared first")

                self.advance()
                machine.start = self.current().value
                self.advance()

            elif token.type == TokenType.ACCEPT:

                if machine is None:
                    raise SyntaxError("Machine must be declared first")

                self.advance()
                machine.accept = self.current().value
                self.advance()

            elif token.type == TokenType.BLANK:

                if machine is None:
                    raise SyntaxError("Machine must be declared first")

                self.advance()
                machine.blank = self.current().value
                self.advance()

            else:

                if machine is None:
                    raise SyntaxError("Machine must be declared first")

                transition = self.parse_transition()
                machine.transitions.append(transition)

        if machine is None:
            raise SyntaxError("Machine declaration not found")

        return machine

    def parse_transition(self) -> TransitionNode:

        state = self.current().value
        self.advance()

        read = self.current().value
        self.advance()

        self.advance()

        next_state = self.current().value
        self.advance()

        write = self.current().value
        self.advance()

        move = self.current().value
        self.advance()

        return TransitionNode(state, read, next_state, write, move)
