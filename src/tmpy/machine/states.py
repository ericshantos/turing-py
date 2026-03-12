# -*- coding: utf-8 -*-
"""
@Author: Eric Santos <ericshantos13@gmail.com>

States implementation for the Turing machine.
"""

from typing import Iterator

from ..exception import InvalidFinalStateError, InvalidInitialStateError


class States:
    def __init__(self, *states: str, initial_state: str, final_states: set[str]):
        self._states = set(states)

        if initial_state not in self._states:
            raise InvalidInitialStateError(initial_state, "Initial state must belong to the state set")

        if not final_states.issubset(self._states):
            raise InvalidFinalStateError(final_states, "Final states must belong to the state set")

        self.initial_state = initial_state
        self.current_state = initial_state
        self.final_states = final_states

    def __contains__(self, state: str) -> bool:
        return state in self._states

    def __iter__(self) -> Iterator[str]:
        return iter(self._states)

    def __len__(self) -> int:
        return len(self._states)

    def __str__(self) -> str:
        return f"Q = {self._states}"
