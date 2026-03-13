# -*- coding: utf-8 -*-
"""
@author: Eric Santos <ericshantos13@gmai.com>

AST node definitions for the Turing machine description language.
"""

from typing import Optional


class MachineNode:

    def __init__(self, name: str):
        self.name = name
        self.start: Optional[str] = None
        self.accept: Optional[str] = None
        self.blank: Optional[str] = None
        self.transitions: list[TransitionNode] = []


class TransitionNode:

    def __init__(self, state, read, next_state, write, move):
        self.state = state
        self.read = read
        self.next_state = next_state
        self.write = write
        self.move = move
