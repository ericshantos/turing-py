# -*- coding: utf-8 -*-
"""
@author: Eric Santos <ericshantos13@gmail.com>

Loader for the Turing machine DSL.
"""

from pathlib import Path

from ..alphabet import Alphabet, Symbol, TapeAlphabet
from ..machine import States, TuringMachine
from ..transition import Direction, Transition, TransitionFunction
from .ast import MachineNode
from .lexer import Lexer
from .parser import Parser
from .token import Token

move_map = {"L": Direction.LEFT, "R": Direction.RIGHT, "S": Direction.STAY}


class MachineLoader:

    @classmethod
    def load(cls, path: str | Path) -> TuringMachine:

        text = cls._read_file(path)
        tokens = cls._lex(text)
        ast = cls._parse(tokens)

        symbols, blank = cls._collect_symbols(ast)

        alphabet, tape_alphabet = cls._build_alphabets(symbols, blank)
        states = cls._build_states(ast)
        delta = cls._build_delta(ast)

        return TuringMachine(states, alphabet, tape_alphabet, delta)

    @classmethod
    def _collect_symbols(cls, ast: MachineNode) -> tuple[set[Symbol], Symbol]:
        symbols: set[Symbol] = set()

        for t in ast.transitions:
            symbols.add(Symbol(t.read))
            symbols.add(Symbol(t.write))

        if ast.blank is None:
            raise ValueError("Blank symbol not defined")

        blank = Symbol(ast.blank)

        return symbols, blank

    @classmethod
    def _build_alphabets(cls, symbols: set[Symbol], blank: Symbol) -> tuple[Alphabet, TapeAlphabet]:
        input_alphabet = Alphabet(*[s for s in symbols if s != blank])
        tape_alphabet = TapeAlphabet(blank, *[s for s in symbols if s != blank])

        return input_alphabet, tape_alphabet

    @classmethod
    def _build_states(cls, ast: MachineNode) -> States:
        states = set()

        for t in ast.transitions:
            states.add(t.state)
            states.add(t.next_state)

        if ast.start is None:
            raise ValueError("Start state not defined")

        if ast.accept is None:
            raise ValueError("Accept state not defined")

        states.add(ast.start)
        states.add(ast.accept)

        return States(
            *states,
            initial_state=ast.start,
            final_states={ast.accept},
        )

    @classmethod
    def _build_delta(cls, ast: MachineNode):
        transitions = []

        for node in ast.transitions:
            transitions.append(
                Transition(
                    node.state,
                    Symbol(node.read),
                    node.next_state,
                    Symbol(node.write),
                    move_map[node.move],
                )
            )

        return TransitionFunction(*transitions)

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
