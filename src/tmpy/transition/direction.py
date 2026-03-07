# -*- coding: utf-8 -*-
"""
@Author: Eric Santos <ericshantos13@gmail.com>

Module for the direction of the transition.
"""


from enum import Enum
from collections.abc import Iterable

class Direction(Enum):
    RIGHT: int = 1
    LEFT: int = -1

    def move(self, head: int) -> int:
        return head + self.value

    def __str__(self) -> str:
        return self.name
    