"""
@author: Eric Santos <ericshantos13@gmail.com>

This module defines the TransitionFunction class, which represents the
transition function of a finite automaton. It allows adding transitions
and retrieving transitions based on the current state and input symbol.
"""

from collections.abc import Iterable

from ..alphabet import Symbol
from .transition import Transition


class TransitionFunction:
    def __init__(self, *args: Transition) -> None:

        self._tr: dict[tuple[str, Symbol], Transition] = {}

        for t in args:

            if isinstance(t, Iterable) and not isinstance(t, Transition):
                for tr in t:
                    self._tr[(tr.state, tr.symbol)] = tr
            else:
                self._tr[(t.state, t.symbol)] = t

    def __call__(self, state: str, symbol: Symbol) -> Transition | None:
        return self._tr.get((state, symbol))

    def __contains__(self, item) -> bool:
        return item in self._tr

    def __str__(self) -> str:
        return "\n".join(str(t) for t in self._tr.values())
