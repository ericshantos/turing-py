"""
@author: Eric Santos <ericshantos13@gmail.com>

This module defines the TransitionFunction class, which represents the 
transition function of a finite automaton. It allows adding transitions 
and retrieving transitions based on the current state and input symbol.
"""


from collections.abc import Iterable
from .transition import Transition
from ..alphabet import Symbol


class TransitionFunction:
    def __init__(self) -> None:
        self._transitions: dict[tuple[str, Symbol], Transition] = {}

    def add(self, *transitions: Transition) -> None:

        for t in transitions:

            if isinstance(t, Iterable) and not isinstance(t, Transition):
                for tr in t:
                    self._transitions[(tr.state, tr.symbol)] = tr
            else:
                self._transitions[(t.state, t.symbol)] = t

    def __call__(self, state: str, symbol: Symbol) -> Transition | None:
        return self._transitions.get((state, symbol))

    def __str__(self) -> str:
        return "\n".join(str(t) for t in self._transitions.values())

    @property
    def conjugates(self) -> dict[tuple[str, str], Transition]:
        return self._transitions
